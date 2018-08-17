from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    カスタムユーザー データ定義クラス
      電話番号などを追加したい場合はこのクラスに追加します。
    """

    # first_name、last_nameは利用せずにfull_nameを使う
    full_name = models.CharField(
        verbose_name='名前',
        max_length=100,
        blank=True
    )

    # このアプリケーションでは利用にあたってログイン必須という前提である。
    # このためスタッフ権限のデフォルトはTrueに変更する
    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
    )

    # get_full_name()のオーバーライド
    def get_full_name(self):
        if self.full_name:
            return self.full_name
        else:
            return self.username + '（名前未設定）'

    # 管理画面・リストボックス表示
    def __str__(self):
        return self.get_full_name()
