class EmailVerifyRecord(models.Model):
    """
    ���伤����
    """
    code = models.CharField(max_length=20, verbose_name='������')
    email=models.EmailField(max_length=50,verbose_name='����')
    send_time=models.DateTimeField(verbose_name='����ʱ��',default=datetime.now)
    class Meta:
        verbose_name='������֤��'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '{0}({1})'.format(self.code,self.email)
