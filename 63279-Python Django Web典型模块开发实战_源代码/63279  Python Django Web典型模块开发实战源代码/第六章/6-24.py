from django.db import models
from datetime import datetime
# Create your models here.
class UserInfo(models.Model):
    """
    �û���
    """
    user_type_chioces=(
        (1,"��ͨ�û�"),
        (2,"VIP"),
        (3,"SVIP"),
    )
    user_type=models.IntegerField(choices=user_type_chioces)
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name='�û���'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
class UserToken(models.Model):
    """
    token��
    """
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    token=models.CharField(max_length=64)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name='token��'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.user.username
class CommonVideo(models.Model):
    """
    ��ͨ��Ƶ
    """
    title=models.CharField(max_length=32)
    url=models.CharField(max_length=200,verbose_name='��Դ��ַ')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name='��ͨ��Ƶ��'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
class VIPVideo(models.Model):
    """
    ��Ա��Ƶ
    """
    title=models.CharField(max_length=32)
    url=models.CharField(max_length=200,verbose_name='��Դ��ַ')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name='��Ա��Ƶ��'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
class SVIPVideo(models.Model):
    """
    ������Ա��Ƶ
    """
    title=models.CharField(max_length=32)
    url=models.CharField(max_length=200,verbose_name='��Դ��ַ')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name='������Ա��Ƶ��'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
