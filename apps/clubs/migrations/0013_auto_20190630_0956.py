# Generated by Django 2.0 on 2019-06-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0012_club_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='required',
            field=models.CharField(choices=[('1', '大一'), ('2', '大二'), ('3', '不限')], default='1', max_length=2, verbose_name='年级要求'),
        ),
    ]
