from django.db import models
# Create your models here.
class Permission(models.Model):
    """
    Ȩ�ޱ�
    """
    url=models.CharField(max_length=64)
    title=models.CharField(max_length=10)
    class Meta:
        verbose_name='Ȩ�ޱ�'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
class Userinfor(models.Model):
    """
    �û���
    """
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    permission = models.ManyToManyField(Permission ,null=True,blank=True)
    class Meta:
        verbose_name = '�û���'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
