from datetime import datetime
# Create your models here.
class TuWen(models.Model):
    """
    ͼ�ı�
    """
    image = models.ImageField(max_length=200, upload_to='images/',verbose_name='ͼƬ')
    title=models.CharField(max_length=200,blank=True,null=True,verbose_name='�ı�')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    class Meta:
        verbose_name = "ͼ����Ϣ"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
