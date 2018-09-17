from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_api.models import Banner1,Category
from rest_api.serializers import *
from rest_api.helper import ConstantMsg
from rest_framework import status




def to_response(data=None,status=status.HTTP_200_OK,msg=ConstantMsg.MSG_STATUS_SUCCESS):
    result={
        'status':status,
        'msg':msg,
        'data':data
    }


class BannerView(APIView):
    def get(self,request):
        banner=Banner1.objects.filter(is_delete=False)
        serializer=BannerSerializer(banner,many=True)
        return Response(data=serializer.data)
    def post(self,request):
        pass


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer: CategroySerializer = CategroySerializer(categories, many=True)
        return to_response(data=serializer.data)
# Create your views here.
