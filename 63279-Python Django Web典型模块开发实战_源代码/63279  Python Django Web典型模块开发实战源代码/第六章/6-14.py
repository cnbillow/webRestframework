from django.shortcuts import render,HttpResponse,redirect
from RBAC.models import User,Permission,Role
# Create your views here.
def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')
        user=User.objects.filter(name=username,pwd=pwd).first()
        if user:
            #��֤���
            request.session["user_id"]=user.pk
            #��ѯ��ɫ
            ret=user.role.all()
            print(ret)#<QuerySet [<Role: ������Դ�ܼ�>]>
            #��ѯ��ɫ����Ӧ��Ȩ��
            re=user.role.all().values('permission__url')
            print(re)#<QuerySet [{'permission__url': '/users/'}]>
            permission_list=[]
            for item in re:
                permission_list.append(item["permission__url"])
            print(permission_list)#['/users/']
            request.session["permission_list"] = permission_list
            return HttpResponse('��¼�ɹ�')
    return render(request, "login.html")
