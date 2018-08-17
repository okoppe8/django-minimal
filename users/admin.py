from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class AdminUserAdmin(UserAdmin):

    # 標準のユーザー管理より以下の点を変更
    # full_nameを追加
    # first_name,last_name, is_staff, groups, user_permissions を非表示

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'full_name')
    list_filter = ('is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'full_name')
