from rest_framework import serializers
from rest_api.models import Banner1,Category,SubMenu
from django.template.context_processors import request

from rest_api.models import Banner1

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner1
        # field='__all__'
        field=['bid','img_url']

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubMenu
        fields='__all__'
        #fields=['bid','img_url']


class CategroySerializer(serializers.ModelSerializer):
    submenu_set=SubSerializer(many=True,allow_null=True)
