from django.shortcuts import render, HttpResponse, redirect
from web import models
from web.utils.md5 import gen_md5
import time


def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'login.html')

    user = request.POST.get('user')
    # pwd = gen_md5(request.POST.get('pwd',''))
    pwd = request.POST.get('pwd', '')

    # 根据用户名和密码去用户表中获取用户对象
    user = models.UserInfo.objects.filter(name=user, password=pwd).first()
    if not user:
        return render(request, 'login.html', {'msg': '用户名或密码错误'})
    request.session['user_info'] = {'id': user.id, 'nickname': user.nickname}
    models.Goods.objects.update(now_time=time.time())
    all_data = models.Goods.objects.all()
    for data in all_data:
        print(data.now_time, type(data.now_time))
    return redirect('/index/')


def logout(request):
    """
    注销
    :param request:
    :return:
    """
    request.session.delete()

    return redirect('/login/')


def index(request):
    return render(request, 'index.html')
