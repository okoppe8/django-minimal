from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    # 名前の追加
    full_name = models.CharField(
        verbose_name='名前',
        max_length=100,
        blank=True
    )

    # 既存メソッドの変更
    def get_full_name(self):
        return self.full_name

    # スタッフ権限のデフォルトをTrueに変更
    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
