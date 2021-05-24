from django.db import models
from rbac.models import UserInfo as RbacUserInfo


class Brand(models.Model):
    '''厂家表'''
    brand_name = models.CharField(verbose_name='厂家名称', max_length=32)

    def __str__(self):
        return self.brand_name


class Goods(models.Model):
    '''商品'''
    commodity_name = models.CharField(verbose_name='商品名称', max_length=32)
    flavor = models.CharField(verbose_name='口味', max_length=32)
    date_of_manufacture = models.DateField(verbose_name='生产日期')
    shelf_data = models.IntegerField(verbose_name='保质期',default=24)
    now_time = models.CharField(verbose_name='当前时间',max_length=32)
    overdue = models.IntegerField(verbose_name='过期天数',default=0)
    brand = models.ForeignKey(verbose_name='品牌', to='Brand', on_delete=True)
    is_put = models.BooleanField(verbose_name='是否上架', default=False)
    is_sell = models.BooleanField(verbose_name='是否出售', default=False)

    def __str__(self):
        return self.commodity_name

class UserInfo(RbacUserInfo):
    """
    员工表
    """
    nickname = models.CharField(verbose_name='姓名', max_length=16)
    phone = models.CharField(verbose_name='手机号', max_length=32)

    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(verbose_name='性别', choices=gender_choices, default=1)
    depart = models.ForeignKey(verbose_name='部门', to="Department",on_delete=True)
    def __str__(self):
        return self.nickname
class Department(models.Model):
    """
    部门表
    """
    title = models.CharField(verbose_name='部门名称', max_length=16)

    def __str__(self):
        return self.title