from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class UserProfile(AbstractUser):
    """
    �û�
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="����")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="�绰")
    class Meta:
        verbose_name = "�û�"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
class Good(models.Model):
    """
    ��Ʒ��
    """
    name=models.CharField(max_length=30,verbose_name='��Ʒ����')
    price=models.FloatField(default=0,verbose_name='��Ʒ�۸�',help_text='��λ��Ԫ')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name='��Ʒ��'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class ShoppingCart(models.Model):
    """
    ���ﳵ
    """
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="�û�")
    good = models.ForeignKey(Good,on_delete=models.CASCADE, verbose_name="��Ʒ")
    nums = models.IntegerField(default=0, verbose_name="��������")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="���ʱ��")
    class Meta:
        verbose_name = '���ﳵ'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s(%d)".format(self.good.name, self.nums)
class OrderInfo(models.Model):
    """
    ����
    """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "�ɹ�"),
        ("TRADE_CLOSED", "��ʱ�ر�"),
        ("WAIT_BUYER_PAY", "���״���"),
        ("TRADE_FINISHED", "���׽���"),
        ("paying", "��֧��"),
    )
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="�û�")
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="������")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="���׺�")
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="����״̬")
    post_script = models.CharField(max_length=200, verbose_name="��������")
    order_mount = models.FloatField(default=0.0, verbose_name="�������")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="֧��ʱ��")
    # �û���Ϣ
    address = models.CharField(max_length=100, default="", verbose_name="�ջ���ַ")
    signer_name = models.CharField(max_length=20, default="", verbose_name="ǩ����")
    singer_mobile = models.CharField(max_length=11, verbose_name="��ϵ�绰")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="���ʱ��")
    class Meta:
        verbose_name = "����"
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.order_sn)
class OrderGoods(models.Model):
    """
    ��������Ʒ����
    """
    order = models.ForeignKey(OrderInfo,on_delete=models.CASCADE, verbose_name="������Ϣ", related_name="goods")
    goods = models.ForeignKey(Good,on_delete=models.CASCADE,verbose_name="��Ʒ")
    goods_num = models.IntegerField(default=0, verbose_name="��Ʒ����")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="���ʱ��")
    class Meta:
        verbose_name = "������Ʒ"
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.order.order_sn)
