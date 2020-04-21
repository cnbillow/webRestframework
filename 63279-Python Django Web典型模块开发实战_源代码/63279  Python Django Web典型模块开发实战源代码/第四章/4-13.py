from django.shortcuts import render,HttpResponse
import json
import re
import datetime
import random
from demo4.settings import APIKEY
#�����û������֤���
from .models import Code,UserProfile
#����Խ���Ƭ��ģ��
from utils.yunpian import YunPian
#����drf����ģ��
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
class SendCodeView(APIView):
    """
    ��ȡ�ֻ���֤��
    """
    def get(self,request):
        phone=request.GET.get('phone')
        if phone:
            #��֤�Ƿ�Ϊ��Ч�ֻ���
            mobile_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
            res = re.search(mobile_pat, phone)
            if res:
                #����ֻ��źϷ����鿴�ֻ����Ƿ�ע���
                had_register=UserProfile.objects.filter(phone=phone)
                if had_register:
                    msg = '�ֻ����ѱ�ע�ᣡ'
                    result = {"status": "402", "data": {'msg': msg}}
                    return HttpResponse(json.dumps(result, ensure_ascii=False),
                                        content_type="application/json,charset=utf-8")
                else:
                    #����Ƿ��͹������û���͹�������֤�룬������͹�����������
                    had_send=Code.objects.filter(phone=phone).last()
                    if had_send:
                        #���������뷢�͹���֤�룬�鿴�����ϴη���ʱ������û�дﵽһ����
                        if had_send.add_time.replace(tzinfo=None)>
(datetime.datetime.now()-datetime.timedelta(minutes=1)):
                            msg = '�����ϴη�����֤�벻��1���ӣ�'
                            result = {"status": "403", "data": {'msg': msg}}
                            return HttpResponse(json.dumps(result,ensure_ascii=False),                                             content_type="application/json,charset=utf-8")
                        else:
                            # ������֤��
                            code = Code()
                            code.phone = phone
                            # ������֤��
                            c = random.randint(1000, 9999)
                            code.code = str(c)
                            # �趨��֤��Ĺ���ʱ��Ϊ20�����Ժ�
                            code.end_time = 
datetime.datetime.now() + datetime.timedelta(minutes=20)
                            code.save()
                            # ���÷���ģ��
                            code = Code.objects.filter(phone=phone).last().code
                            yunpian = YunPian(APIKEY)
                            sms_status = yunpian.send_sms(code=code, mobile=phone)
                            msg = sms_status
                            return HttpResponse(msg)
                    else:
                        #������֤��
                        code = Code()
                        code.phone = phone
                        #������֤��
                        c = random.randint(1000, 9999)
                        code.code = str(c)
                        #�趨��֤��Ĺ���ʱ��Ϊ20�����Ժ�
                        code.end_time=datetime.datetime.now()+datetime.timedelta(minutes=20)
                        code.save()
                        #���÷���ģ��
                        code = Code.objects.filter(phone=phone).last().code
                        yunpian = YunPian(APIKEY)
                        sms_status = yunpian.send_sms(code=code, mobile=phone)
                        msg = sms_status
                        # print(msg)
                        return HttpResponse(msg)
            else:
                msg = '�ֻ��Ų��Ϸ���'
                result = {"status": "403", "data": {'msg': msg}}
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="application/json,charset=utf-8")
        else:
            msg = '�ֻ���Ϊ�գ�'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
