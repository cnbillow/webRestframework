from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    """
    �û�
    """
    APIkey=models.CharField(max_length=30,verbose_name='APIkey',default='abcdefghigklmn')
    money=models.IntegerField(default=10,verbose_name='���')
    class Meta:
        verbose_name='�û�'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
