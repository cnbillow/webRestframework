import re
from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin
class ValidPermission(MiddlewareMixin):
    """
    Ȩ����֤�м����
    """
    def process_request(self,request):
        ######################�м������start###############
        # ��ȡsession��ֵ����������ڲ���������[]
        permission_list = request.session.get('permission_list', [])
        # print(permission_list)
        path = request.path_info
        # print(path)
        flag = False
        for permission in permission_list:
            permission = "^%s$" % permission
            ret = re.match(permission, path)
            if ret:
                flag = True
                break
        # print(flag)
        if not flag:
            return HttpResponse('�޷���Ȩ�ޣ�')
        ##################�м������end###################
        return None
