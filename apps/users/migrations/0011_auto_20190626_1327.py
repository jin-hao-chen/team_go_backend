# Generated by Django 2.0 on 2019-06-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190626_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='clubs',
            field=models.ManyToManyField(blank=True, null=True, to='clubs.Club', verbose_name='加入的社团'),
        ),
    ]
