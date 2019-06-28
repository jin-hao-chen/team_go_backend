from django.db import models
from users.models import User
from clubs.models import Club


class Apply(models.Model):

    user = models.ForeignKey(to=User, verbose_name='学生', on_delete=models.CASCADE)
    club = models.ForeignKey(to=Club, verbose_name='社团', on_delete=models.CASCADE)
    department_name = models.CharField(max_length=30, verbose_name='部门名', default='任意部门')

    class Meta:
        verbose_name = '申请社团'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '申请'


class Follow(models.Model):

    user = models.ForeignKey(to=User, verbose_name='学生', on_delete=models.CASCADE)
    club = models.ForeignKey(to=Club, verbose_name='社团', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '关注社团'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '关注'
