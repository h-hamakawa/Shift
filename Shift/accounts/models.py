from django.db import models


class AdminSetting(models.Model):

    employee_number = models.CharField(
        max_length=50,
        verbose_name='従業員番号',
    )
    password = models.CharField(
        max_length=128,
        verbose_name='パスワード',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='作成日時',
    )

    class Meta:
        verbose_name = '管理者設定'
        verbose_name_plural = '管理者設定'

    def __str__(self):
        return f'管理者: {self.employee_number}'
