from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
# Create your views here.
class IndexView(APIView):
    """
    ��ʾ��ͼ
    """
    throttle_classes = (AnonRateThrottle,)
    def get(self,request):
        return Response('����ҳ������������������ܴ����������ҳ��')
