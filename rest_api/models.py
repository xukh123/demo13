from django.db import models

class Banner1(models.Model):
    bid = models.AutoField(primary_key=True)
    img_url = models.CharField(max_length=100)
    detail_url = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'banner1'
        ordering = ['-bid']

class Category(models.Model):
    cate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'category'


class SubMenu(models.Model):
    sub_menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    cate = models.ForeignKey('Category', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'sub_menu'

# Create your models here.
