from django.shortcuts import render,HttpResponse,redirect
from .models import Userinfor,Permission
# Create your views here.
def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')
        user=Userinfor.objects.filter(name=username,pwd=pwd).first()
        if user:
            #��֤���
            request.session["user_id"]=user.pk
            return HttpResponse('��¼�ɹ�')
    return render(request, "login.html")
def userinfo(request):
    #���Ƚ��������֤
    pk=request.session.get('user_id')
    if not pk:
        return redirect("/login/")
    #Ȼ�����Ȩ����֤
    user=Userinfor.objects.filter(id=pk).first()
    p_list = []
    p_queryset = user.permission.all()
    #��ȡ�û���Ȩ���б�
    for p in p_queryset:
        p_list.append(p.url)
    #ȥ��
    p_list=list(set(p_list))
    # print(p_list)
    # ��ȡURL
    c = request.path_info
    if c in p_list:
        u_queryset=Userinfor.objects.all()
        return render(request,"userinfo.html",{ "u_queryset":u_queryset})
    else:
        return HttpResponse('û��Ȩ�޷��ʸ�ҳ��')
