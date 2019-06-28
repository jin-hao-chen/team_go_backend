# Generated by Django 2.0 on 2019-06-28 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190626_1327'),
        ('clubs', '0008_auto_20190626_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserClubAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '用户社团管理员表',
                'verbose_name_plural': '用户社团管理员表',
            },
        ),
        migrations.AlterField(
            model_name='club',
            name='level',
            field=models.CharField(choices=[('1', '校级'), ('2', '院级'), ('3', '无(特殊用途)')], default=1, max_length=10, verbose_name='等级'),
        ),
        migrations.AddField(
            model_name='userclubadmin',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.Club', verbose_name='社团'),
        ),
        migrations.AddField(
            model_name='userclubadmin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='用户'),
        ),
    ]