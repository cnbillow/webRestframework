class Code(models.Model):
    """
    ��֤��
    """
    phone=models.CharField(max_length=11,verbose_name='�ֻ���')
    code=models.CharField(max_length=4,verbose_name='��֤��')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='���ʱ��')
    end_time = models.DateTimeField(default=datetime.now, verbose_name='����ʱ��')
    class Meta:
        verbose_name='��֤���'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.phone
