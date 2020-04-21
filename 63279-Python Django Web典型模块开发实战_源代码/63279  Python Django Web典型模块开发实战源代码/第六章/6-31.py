from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
#�����������ݱ�
from .models import *
�����������л���
from .serializers import *
#����drf���ģ��
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework import exceptions
# Create your views here.
class Authtication(object):
    def authenticate(self,request):
        # ��֤�Ƿ��Ѿ���¼,����������Ϊ��authenticate
        token = request._request.GET.get('token')
        token_obj=UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('�û���֤ʧ�ܡ�')
        #��rest_framework�ڲ��Ὣ��������Ԫ�ظ�ֵ��request���Թ�����ʹ��
        return (token_obj.user,token_obj)
    def authenticate_header(self,request):
        #�����������û���ݣ����Ǳ���Ҫ��
        pass
class CommonVideoView(APIView):
    """
    ��¼�󼴿ɷ��ʵ�������Դ
    """
    renderer_classes = [JSONRenderer]  # ��Ⱦ��
    authentication_classes = [Authtication,]
    def get(self,request):
        # print(request.user,request.auth)#user1 user1
        video_list = CommonVideo.objects.all()
        re = CommonVideoSerializer(video_list, many=True)
        return Response(re.data)
#��������
