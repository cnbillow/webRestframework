def login(request):
    message = ""
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = Administrator.objects.filter(username=user, password=pwd).count()
        if c:
			#����
            rep = redirect('index.html')
            rep.set_signed_cookie('username', user)
            rep.set_signed_cookie('password', pwd)
            return rep
        else:
            message = "�û������������"
    return render(request,'login.html', {'msg': message})
def index(request):
    # ����û��Ѿ���¼����ȡ��ǰ��¼���û���
    # ���򣬷��ص�¼ҳ��
    username = request.get_signed_cookie('username')
    password = request.get_signed_cookie('password')
    c = Administrator.objects.filter(username=username, password=password).count()
    if c:
        return render(request, 'index.html', {'username': username})
    else:
        return redirect('/login.html')
