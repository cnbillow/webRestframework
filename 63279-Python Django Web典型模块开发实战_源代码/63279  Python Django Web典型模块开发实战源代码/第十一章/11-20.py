from django.db import models
# Create your models here.
class Goods(models.Model):
    """
    ��Ʒ��
    """
    title=models.CharField(max_length=64,verbose_name='��Ʒ��')
    pv=models.IntegerField(default=0,verbose_name='�����')
    class Meta:
        verbose_name='��Ʒ��'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
