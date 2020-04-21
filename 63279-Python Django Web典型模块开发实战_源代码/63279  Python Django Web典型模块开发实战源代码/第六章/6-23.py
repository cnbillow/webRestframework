from django.shortcuts import render,HttpResponse,redirect
from RBAC.models import User,Permission,Role
# Create your views here.
from RBAC.service.permission import initial_permission
def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')
        user=User.objects.filter(name=username,pwd=pwd).first()
        if user:
            #��֤���
            request.session["user_id"]=user.pk
            initial_permission(user,request)
            return HttpResponse('��¼�ɹ�')
    return render(request, "login.html")
