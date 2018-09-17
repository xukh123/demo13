# 将模型对象转化字段
import datetime
from decimal import Decimal


def model_to_dict(obj):
    dic = {}
    # 将传进来的对象的所有的属性获取到
    for key in vars(obj).keys():
        if not key.startswith("_"):
            # 通过对象的key获取所对应的值
            value = getattr(obj, key)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(value, datetime.date):
                value = value.strftime('%Y-%m-%d')
            elif isinstance(value, Decimal):
                value = float(value)
            dic[key] = value
    return dic


def to_list(objs):
    li = []
    if objs:
        for obj in objs:
            li.append(model_to_dict(obj))
    return li
