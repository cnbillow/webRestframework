from .utils.alipay import AliPay
from demo10.settings import private_key_path,ali_pub_key_path
class ShopView(LoginRequiredMixin,View):
    """
    ������ͼ
    """
    def get(self,request):
        return render(request,'shop.html',{'user':request.user})
    def post(self,request):
        alipay = AliPay(
            appid="2016091400509946",
            app_notify_url="http://127.0.0.1:8000/shop/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # ֧�����Ĺ�Կ����֤֧�����ش���Ϣʹ�ã��������Լ��Ĺ�Կ,
            debug=True,  # Ĭ��False,
            return_url="http://127.0.0.1:8000/shop/"
        )
        url = alipay.direct_pay(
            #����ǰ�˽��������ݣ�ȷ��subject����Ʒ���ƣ������ɲ��ظ��Ľ��׺�out_trade_no,
            # ������Ʒ����������ܼ�total_amount
            subject="��ı���",
            out_trade_no="20190316sss1",
            total_amount=100,
            return_url="http://127.0.0.1:8000/alipay/return/"
        )
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
        print(re_url)
        return redirect(re_url)
