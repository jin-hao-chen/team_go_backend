# Generated by Django 2.0 on 2019-06-26 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190626_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='clubs',
            field=models.ManyToManyField(to='clubs.Club', verbose_name='加入的社团'),
        ),
    ]
