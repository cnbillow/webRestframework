from ..models import *
from rest_framework import exceptions
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
