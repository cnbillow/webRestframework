def login(request):
#��¼����
    if request.method == "POST":
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')
        user=User.objects.filter(name=username,pwd=pwd).first()
        if user:
            #��֤���
            request.session["user_id"]=user.pk
            #��ѯ��ɫ
            ret=user.role.all()
            # print(ret)#<QuerySet [<Role: ������Դ�ܼ�>]>
            #��ѯ��ɫ����Ӧ��Ȩ��
            permission_list = []
            for item1 in ret:
                #��Զ������ѯ
                rep =Permission.objects.filter(role__title=item1)
                for item2 in rep:
                    # print(item2.url)#/users/
                    permission_list.append(item2.url)
            # print(permission_list)
            request.session["permission_list"] = permission_list
            return HttpResponse('��¼�ɹ�')
    return render(request, "login.html")
