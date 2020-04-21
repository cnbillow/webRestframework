from utils import email_send
class SendActiveCodeView(APIView):
    """
    ���ͼ���������
    """
    def get(self,request):
        email=request.GET.get('email')
        if email:
            email_send.send_register_email(email)
            msg = '���������ѷ��Ͷ��������䣬��ǰ��������ɼ��'
            result = {"status": "200", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        else:
            msg = 'δ�յ����䣡'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
from .models import EmailVerifyRecord
class ActiveView(APIView):
    """
    ������֤�û���
    """
    def get(self,request,code):
        item=EmailVerifyRecord.objects.filter(code=code).last()
        if item:
            email=item.email
            user=UserProfile.objects.filter(email=email).first()
            user.is_auther=True
            user.save()
            msg='����֤Ϊ�����ߣ����Դ���Ӧ������'
            result = {"status": "200", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        else:
            msg = '��֤ʧ��'
            result = {"status": "403", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
