from Django.db import models
from datetime import datetime
# Create your models here.
class Type1(models.Model):
    """
    һ����Ŀ
    """
    name=models.CharField(max_length=10,default="",verbose_name="��Ŀ��")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name = '��Ʒ���'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class Type2(models.Model):
    """
    ������Ŀ
    """
parent=models.ForeignKey(Type1,verbose_name="�������",
null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=10,default="",verbose_name="��Ŀ��")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name = '��Ʒ���2'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class Type3(models.Model):
    """
    ������Ŀ
    """
parent=models.ForeignKey(Type2,verbose_name="�������",
null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=10,default="",verbose_name="��Ŀ��")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name = '��Ʒ���3'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class Type4(models.Model):
    """
    �ļ���Ŀ
    """
parent=models.ForeignKey(Type3,verbose_name="�������",
null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=10,default="",verbose_name="��Ŀ��")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name = '��Ʒ���4'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
