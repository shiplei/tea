# Generated by Django 2.2.18 on 2021-05-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_auto_20210516_2123'),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.CharField(max_length=32, verbose_name='邮箱')),
                ('nickname', models.CharField(max_length=16, verbose_name='姓名')),
                ('phone', models.CharField(max_length=32, verbose_name='手机号')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别')),
                ('roles', models.ManyToManyField(blank=True, to='rbac.Role', verbose_name='拥有的所有角色')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
