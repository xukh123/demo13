from django.db import models
from django.db import models


# 1>json数据
# 1.1>数据格式如何转化成json
# 2>前后端分离跟不分离的请求的区别
# 前后端分离  xml
# 后台只提供数据  移动端---提供数据      后台--->提供数据(json) 前端 ----> 移动端
# 性能提升了
# 前端不分离   用户发送请求---->路由--->视图--->从数据库获取数据---->渲染--- 返回给客服端
# 前后端分离   发送请求--->请求html文件--客服端--->浏览器解析html --->ajax发送请求 ---->视图----> 从数据库获取数据----->转化json数据--->返回json数据
# --->客服端dom操作---->刷界面---->显示数据

# restful
# 一种设计风格  主要用来做前端分离的一种技术,针对是我们的api如何设计,对返回数据格式的设计
# result = {
#     'status': 200,
#     'msg': 'success',
#     'data': {} 或者[]
# }

class Banner(models.Model):
    bid = models.AutoField(primary_key=True)
    img_url = models.CharField(max_length=100)
    detail_url = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'banner'
        ordering = ['-bid']

# Create your models here.
