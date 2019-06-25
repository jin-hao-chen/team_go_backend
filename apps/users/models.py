from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from users.validators import validate_username
from clubs.models import Institute
from clubs.models import Club
# from ckeditor_uploader.fields import RichTextUploadingField
from DjangoUeditor.models import UEditorField


class AdminInfo(AbstractUser):
    """后台管理员表

    Notes
    -----
    AdminInfo 和 学生表是分开来的, AdminInfo 是提供给后台内部使用的
    一般用于后台统计数据, 导出统计数据文件等, 因此 AdminInfo 只包含了
    少数的字段
    """
    username = models.CharField(max_length=10, validators=[validate_username], verbose_name='学号', unique=True)
    password = models.CharField(_('密码'), max_length=128)
    nickname = models.CharField(max_length=30, verbose_name='昵称', blank=True, null=True)
    mobile = models.CharField(max_length=11, verbose_name='手机号', blank=True, null=True)
    email = models.EmailField(_('邮箱'), blank=True)

    class Meta:
        verbose_name = '管理员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class Teacher(models.Model):
    username = models.CharField(max_length=10, validators=[validate_username], verbose_name='工号', unique=True, \
                                null=False, blank=False)
    nickname = models.CharField(max_length=20, verbose_name='老师名', null=False, blank=False)
    mobile = models.CharField(max_length=11, verbose_name='手机号', null=False, blank=False)
    club = models.OneToOneField(to=Club, on_delete=models.CASCADE, verbose_name='指导的社团', null=True)

    class Meta:
        verbose_name = '指导老师'
        verbose_name_plural = '指导老师'

    def __str__(self):
        return self.username


class User(models.Model):

    username = models.CharField(max_length=10, validators=[validate_username], verbose_name='学号', unique=True)
    password = models.CharField(verbose_name='密码', max_length=128, blank=False, null=False)
    nickname = models.CharField(max_length=30, verbose_name='学生名', blank=False, null=False)
    mobile = models.CharField(max_length=11, verbose_name='手机号', null=True, blank=True)
    is_admin = models.BooleanField(verbose_name='是否为管理员', null=False, blank=False, default=False)
    institute = models.ForeignKey(to=Institute, on_delete=models.CASCADE, verbose_name='所属学院', null=False, blank=False)
    admission_time = models.DateField(verbose_name='入学时间', null=False, blank=False)
    # introduction = models.TextField(max_length=100, verbose_name='个人简介')
    introduction = UEditorField(verbose_name='个人简介', width=600, height=300, toolbars="full")
    icon = models.ImageField(upload_to='media/images/users/icons', null=True, blank=True)
    clubs = models.ManyToManyField(to=Club, verbose_name='加入的社团')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username
