class RegisterView(APIView):
    """
    ע����
    """
    def get(self,request):
        username=request.GET.get('username')
        pwd=request.GET.get('pwd')
        phone=request.GET.get('phone')
        email=request.GET.get('email')
        code=request.GET.get('code')
        if username:
            pass
        else:
            msg = '�û�������Ϊ�գ�'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        if pwd:
            pass
        else:
            msg = '���벻��Ϊ�գ�'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        if phone:
            pass
        else:
            msg = '�ֻ��Ų���Ϊ�գ�'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        if email:
            pass
        else:
            msg = '���䲻��Ϊ�գ�'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        if code:
            pass
        else:
            msg = '��֤�벻��Ϊ�գ�'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        #���ҶԱ���֤��
        code1=Code.objects.filter(phone=phone).last()
        if code==code1:
            #��֤��֤���Ƿ��Ѿ�����
            end_time=code1.end_time
            end_time=end_time.replace(tzinfo=None)
            if end_time > datetime.datetime.now():
                user = UserProfile()
                user.username = username
                user.password = pwd
                user.phone = phone
                user.email=email
                user.save()
                msg = 'ע��ɹ���'
                result = {"status": "200", "data": {'msg': msg}}
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="application/json,charset=utf-8")
            else:
                msg = '��֤���ѹ��ڣ�'
                result = {"status": "403", "data": {'msg': msg}}
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="application/json,charset=utf-8")
        else:
            msg = '��֤�����'
            result = {"status": "403", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
