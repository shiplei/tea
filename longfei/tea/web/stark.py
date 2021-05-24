from stark.service.v1 import site
from web import models
from web.views.brand import BrandHandler
from web.views.goodsisput import Goodsisput
from web.views.goodsisnotput import Goodsisnotput
from web.views.userinfo import UserInfoHandler
#
#
# # site.register(models.UserInfo, UserInfoHandler)
site.register(models.UserInfo, UserInfoHandler)
site.register(models.Brand, BrandHandler)
site.register(models.Goods, Goodsisput, 'iput')
site.register(models.Goods, Goodsisnotput, 'nput')
