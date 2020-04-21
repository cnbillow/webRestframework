from datetime import datetime
from django.db import models
class Book(models.Model):
    """
    �鼮��Ϣ
    """
    title=models.CharField(max_length=30,verbose_name='����',default='')
    isbn=models.CharField(max_length=30,verbose_name='isbn',default='')
    author=models.CharField(max_length=20,verbose_name='����',default='')
    publish=models.CharField(max_length=30,verbose_name='������',default='')
    rate=models.FloatField(default=0,verbose_name='��������')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name='�鼮��Ϣ'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
