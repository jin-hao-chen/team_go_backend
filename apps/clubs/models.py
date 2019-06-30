import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


class Institute(models.Model):

    name = models.CharField(max_length=20, verbose_name='学院名称', null=False, blank=False, unique=True)

    class Meta:
        verbose_name = '学院'
        verbose_name_plural = '学院'

    def __str__(self):
        return self.name


class Club(models.Model):

    name = models.CharField(max_length=30, verbose_name='社团名', null=False, blank=False, unique=True)
    create_time = models.DateField(verbose_name='创建时间', default=datetime.date.today)
    brief = models.TextField(max_length=100, verbose_name='社团简介', null=False, blank=False, default='')
    description = UEditorField(verbose_name='社团描述', width=600, height=300, toolbars="full",
                               imagePath="images/clubs/descriptions/", filePath="files/clubs/descriptions/")
    icon = models.ImageField(upload_to='images/clubs/icons/', null=True, blank=True)
    TYPE_CHOICES = (
        ('1', '学术'),
        ('2', '学艺'),
        ('3', '体育'),
        ('4', '服务'),
        ('5', '康乐'),
        ('6', '综合'),
        ('7', '资质'),
        ('8', '其他'),
        ('9', '无(特殊用途)')
    )
    type = models.CharField(max_length=10, verbose_name='社团类型', choices=TYPE_CHOICES, null=False, blank=False, default=1)
    LEVEL_CHOICES = (
        ('1', '校级'),
        ('2', '院级'),
        ('3', '无(特殊用途)')
    )
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, null=False, blank=False, default=1, verbose_name='等级')
    persons = models.IntegerField(verbose_name='社团人数', default=0)
    REQUIRED_CHOICE = (
        ('1', '大一'),
        ('2', '大二'),
        ('3', '不限')
    )
    required = models.CharField(max_length=2, choices=REQUIRED_CHOICE, default='1', verbose_name='年级要求')

    class Meta:
        verbose_name = '社团'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Notification(models.Model):

    title = models.CharField(max_length=30, verbose_name='推送标题')
    image = models.ImageField(upload_to='clubs/notifications/', verbose_name='推送图片')
    content = UEditorField(verbose_name='内容')
    publish_date = models.DateField(verbose_name='发布时间', default=datetime.date.today)
    club = models.ForeignKey(to=Club, on_delete=models.CASCADE, verbose_name='社团', default=None)

    class Meta:
        verbose_name = '社团推送'
        verbose_name_plural = '社团推送'

    def __str__(self):
        return '社团推送'


class UserClub(models.Model):

    """
    在此表中的用户都是管理员
    """
    user = models.ForeignKey(to='users.User', verbose_name='用户', on_delete=models.CASCADE)
    club = models.ForeignKey(to=Club, verbose_name='社团', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '用户社团管理员表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户社团管理员表'
