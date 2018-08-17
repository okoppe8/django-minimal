from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class AdminUserAdmin(UserAdmin):

    # first_name,last_nameを非表示にして full_nameを追加
    # マイクロシステムに不要なパーミッション設定を非表示（is_staff, groups, user_permissions）

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'full_name')
    list_filter = ('is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'full_name')
