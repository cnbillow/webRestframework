from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import *
# Create your views here.
def md5(user):
    import hashlib
    import time
    ctime=str(time.time())
    m=hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()
class AuthView(APIView):
    """
    ��¼
    """
    def post(self,request):
        ret={'code':1000,'msg':'��¼�ɹ���'}
        try:
            user=request._request.POST.get('username')
            pwd=request._request.POST.get('password')
            obj=UserInfo.objects.filter(username=user,password=pwd).first()
            if not obj:
                ret['code']=1001
                ret['msg']='�û������������'
                return JsonResponse(ret)
            #Ϊ��¼�û�����token
            token=md5(user)
            #��������£������ڵĴ���
            UserToken.objects.update_or_create(user=obj,defaults={'token':token})
            ret['token']=token
        except Exception as e:
            ret['code']=1002
            ret['msg']='�����쳣'
        return JsonResponse(ret)
