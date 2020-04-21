from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class UserProfile(AbstractUser):
    """
    �û���
    """
    user_type_chioces = (
        (1, "��ͨ�û�"),
        (2, "����"),
        (3, "����Ա"),
    )
    level = models.IntegerField(choices=user_type_chioces,default=1)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name='�û�'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
class Article(models.Model):
    """
    ���±�
    """
    title=models.CharField(max_length=30,verbose_name='����')
    content=models.CharField(max_length=5000,verbose_name='��������')
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name='����'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
