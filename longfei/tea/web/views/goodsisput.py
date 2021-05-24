from stark.service.v1 import StarkHandler, StarkModelForm, Option
from stark.forms.widgets import DateTimePickerInput
from web import models
from django.utils.safestring import mark_safe
import time


class GoodsisputModelForm(StarkModelForm):
    class Meta:
        model = models.Goods
        fields = '__all__'
        widgets = {
            'date_of_manufacture': DateTimePickerInput,
        }
        exclude = ['is_put', ]


class Goodsisput(StarkHandler):
    def display_nowtime(self, obj=None, is_header=None):
        if is_header:
            return '当前时间'
        return mark_safe("%s" % time.time())

    list_display = [StarkHandler.display_checkbox, 'brand', 'commodity_name', 'flavor', 'date_of_manufacture',
                    'shelf_data','now_time']
    search_list = ['commodity_name__contains', 'flavor__contains']

    search_group = [
        Option(field='brand'),
        Option(field='flavor'),
        # Option(field='date_of_manufacture'),
    ]

    def get_queryset(self, request, *args, **kwargs):
        return self.model_class.objects.filter(is_put=True)

    model_form_class = GoodsisputModelForm

    def action_multi_apply(self, request, *args, **kwargs):
        pk_list = request.POST.getlist('pk')
        models.Goods.objects.filter(id__in=pk_list).update(is_put=False)

    action_multi_apply.text = "下架商品"

    action_list = [action_multi_apply, ]
