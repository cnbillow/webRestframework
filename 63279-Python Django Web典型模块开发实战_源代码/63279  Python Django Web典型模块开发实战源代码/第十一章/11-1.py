from django.db import models
# Create your models here.
class Books(models.Model):
    """
    ͼ���
    """
    title=models.CharField(max_length=64,verbose_name='����')
    pv=models.IntegerField(default=0,verbose_name='�����')
    class Meta:
        verbose_name='ͼ���'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
