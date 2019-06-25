from django.db import models
from DjangoUeditor.models import UEditorField


class Institute(models.Model):

    name = models.CharField(max_length=20, verbose_name='学院名称', null=False, blank=False, unique=True)

    class Meta:
        verbose_name = '学院'
        verbose_name_plural = '学院'

    def __str__(self):
        return self.name


class Notification(models.Model):

    title = models.CharField(max_length=30, verbose_name='推送标题')
    image = models.ImageField(upload_to='clubs/notifications/', verbose_name='推送图片')
    content = models.TextField(max_length=3000, verbose_name='推送内容')
    publish_date = models.DateField(verbose_name='发布时间')

    class Meta:
        verbose_name = '社团推送'
        verbose_name_plural = '社团推送'

    def __str__(self):
        return '社团推送'


class Club(models.Model):

    name = models.CharField(max_length=30, verbose_name='社团名', null=False, blank=False, unique=True)
    create_time = models.DateField(verbose_name='创建时间', null=False, blank=False)
    brief = models.TextField(max_length=100, verbose_name='社团简介', null=False, blank=False, default='')
    description = models.TextField(max_length=3000, verbose_name='社团描述', null=False, blank=False, default='')
    icon = models.ImageField(upload_to='images/clubs/icons/', default='default.jpeg')
    TYPE_CHOICES = (
        (1, '学术'),
        (2, '学艺'),
        (3, '体育'),
        (4, '服务'),
        (5, '康乐'),
        (6, '综合'),
        (7, '资质'),
        (8, '其他')
    )
    type = models.CharField(max_length=10, verbose_name='社团类型', choices=TYPE_CHOICES, null=False, blank=False, default=1)
    LEVEL_CHOICES = (
        (1, '校级'),
        (2, '院级')
    )
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, null=False, blank=False, default=1)
    notifications = models.ForeignKey(to=Notification, on_delete=models.CASCADE, verbose_name='推送', default=None)

    class Meta:
        verbose_name = '社团'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
