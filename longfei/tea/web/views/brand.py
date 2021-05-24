from stark.service.v1 import StarkHandler


class BrandHandler(StarkHandler):
    list_display = ['brand_name', ]
    search_list = ['brand_name__contains']
