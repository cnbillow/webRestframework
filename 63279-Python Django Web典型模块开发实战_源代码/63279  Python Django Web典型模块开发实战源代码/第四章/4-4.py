from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    """
    �û�
    """
    is_auther=models.BooleanField(default=False,verbose_name='�Ƿ���֤')
    phone=models.CharField(max_length=11,verbose_name='�绰')
    email = models.CharField(max_length=100,null=True,blank=True,verbose_name='����')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name='�û�'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
class Key(models.Model):
    """
    key��
    """
author=models.ForeignKey(UserProfile,verbose_name='������',
on_delete=models.CASCADE)
    app_name=models.CharField(max_length=10,verbose_name='Ӧ������')
    key=models.CharField(max_length=32,verbose_name='Ӧ��keyֵ')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name='key��'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.key
