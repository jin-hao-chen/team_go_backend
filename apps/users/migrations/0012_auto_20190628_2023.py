# Generated by Django 2.0 on 2019-06-28 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190626_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='introduction',
            field=models.TextField(max_length=3000, verbose_name='个人简介'),
        ),
    ]