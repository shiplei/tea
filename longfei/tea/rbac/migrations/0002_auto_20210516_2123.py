# Generated by Django 2.2.18 on 2021-05-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='menu',
            field=models.ForeignKey(blank=True, help_text='null表示不是菜单;非null表示是二级菜单', null=True, on_delete=True, to='rbac.Menu', verbose_name='所属菜单'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='pid',
            field=models.ForeignKey(blank=True, help_text='对于非菜单权限需要选择一个可以成为菜单的权限，用户做默认展开和选中菜单', null=True, on_delete=True, related_name='parents', to='rbac.Permission', verbose_name='关联的权限'),
        ),
    ]