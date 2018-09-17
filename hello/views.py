import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# 使用前后端分离技术
from hello.helper import model_to_dict, to_list
from hello.models import Banner

"""
字典
列表
字符串
数字类型
bool类型
None

# 不支持的类型  模型对象 时间   decimal 

"""


# 返回json数据的时候
# 要么是对象 {字典} 要么就是数组[列表]


def banner(request):
    result = {
        'status': 200,
        'msg': 'success',
    }
    try:
        banners = Banner.objects.filter(is_delete=False)
        data = to_list(banners)
        result.update(data=data)
    except:
        result.update(status=404, msg='资源文件不存在')
        return JsonResponse(result)
    return JsonResponse(result, safe=False)
# Create your views here.
