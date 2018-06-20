from django.db import models

from users.models import User


class Item(models.Model):
    sample = models.CharField(
        verbose_name='サンプル',
        max_length=20,
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='登録者',
        editable=False,
    )

    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.sample

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'
