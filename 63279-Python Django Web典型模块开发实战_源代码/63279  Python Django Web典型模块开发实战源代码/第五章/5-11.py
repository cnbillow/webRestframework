from django.shortcuts import render,redirect,HttpResponse
from .models import Administrator
# Create your views here.
def login(request):
    message = ""
    if request.method == "POST":
        request.session['is_login'] = True
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = Administrator.objects.filter(username=user, password=pwd).count()
        if c:
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/index.html')
            return rep
        else:
            message = "�û������������"
    return render(request,'login.html', {'msg': message})
def auth(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login')
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('/login.html')
    return inner
@auth
def index(request):
    # ����û��Ѿ���¼����ȡ��ǰ��¼���û���
    # ���򣬷��ص�¼ҳ��
    print(666)
    username = request.session.get('username')
    c = Administrator.objects.filter(username=username).count()
    if c:
        return render(request, 'index.html', {'username': username})
    else:
        return redirect('/login.html')
def logout(request):
    request.Session.clear()
    return redirect('/login.html')
