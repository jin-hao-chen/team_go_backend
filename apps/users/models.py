from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from users.validators import validate_username


class AdminInfo(AbstractUser):
    """后台管理员表

    Notes
    -----
    AdminInfo 和 学生表是分开来的, AdminInfo 是提供给后台内部使用的
    一般用于后台统计数据, 导出统计数据文件等, 因此 AdminInfo 只包含了
    少数的字段
    """
    username = models.CharField(max_length=10, validators=[validate_username], verbose_name='学号', unique=True)
    password = models.CharField(max_length=128, verbose_name='密码')
    nickname = models.CharField(max_length=30, verbose_name='昵称', blank=True, null=True)
    mobile = models.CharField(max_length=11, verbose_name='手机号', blank=True, null=True)
    email = models.EmailField(_('邮箱'), blank=True)

    class Meta:
        verbose_name = '管理员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname

