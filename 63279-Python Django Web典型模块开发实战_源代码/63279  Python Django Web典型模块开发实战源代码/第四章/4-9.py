import requests
class YunPian(object):
    def __init__(self,api_key):
        self.api_key=api_key
        self.single_send_url='https://sms.yunpian.com/v2/sms/single_send.json'
    def send_sms(self,code,mobile):
        parmas={
            'apikey':self.api_key,
            'mobile':mobile,
            'text':'��**����������֤����{code}����Ǳ��˲���������Ա�����'.format(code=code)
        }
        #text����Ҫ����Ƭ��̨��ģ������ ����һ�£���Ȼ���Ͳ���ȥ��
        r=requests.post(self.single_send_url,data=parmas)
        print(r)
if __name__=='__main__':
    yun_pian=YunPian('***************�����apikey��')
    yun_pian.send_sms('***����֤�룩','*******���ֻ��ţ�')
