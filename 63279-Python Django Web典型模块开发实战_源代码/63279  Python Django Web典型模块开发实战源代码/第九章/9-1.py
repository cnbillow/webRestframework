from django.db import models
from datetime import datetime
# Create your models here.
class Book(models.Model):
    """
    �鼮
    """
    title=models.CharField(max_length=32,verbose_name='����')
    author=models.CharField(max_length=10,verbose_name='������')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name='�鼮��'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
