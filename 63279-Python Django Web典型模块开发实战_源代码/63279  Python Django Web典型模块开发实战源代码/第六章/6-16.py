import re
def user(request):
    #��ȡsession��ֵ����������ڲ���������None
    permission_list=request.session.get('permission_list',[])
    # print(permission_list)
    path=request.path_info
    # print(path)
    flag=False
    for permission in permission_list:
        permission="^%s$"%permission
        ret=re.match(permission,path)
        if ret:
            flag=True
            break
    # print(flag)
    if not flag:
        return HttpResponse('�޷���Ȩ�ޣ�')
    return HttpResponse('�鿴�û�')
