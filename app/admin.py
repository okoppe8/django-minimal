from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'アイテム'
