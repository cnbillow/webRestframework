class Type(models.Model):
    """
    ��Ʒ���
    """
    CATEGORY_TYPE=(
        (1,'һ����Ŀ'),
        (2,'������Ŀ'),
        (3,'������Ŀ'),
        (4,'�ļ���Ŀ')
    )
    name=models.CharField(default='',max_length=30,verbose_name='�����',help_text='�����')
    code=models.CharField(default='',max_length=30,verbose_name='���code',help_text='���code')
    desc=models.CharField(default='',max_length=30,verbose_name='�������',help_text='�������')
    category_type=models.IntegerField(choices=CATEGORY_TYPE,verbose_name='�������',help_text='�������')
    parent_category=models.ForeignKey('self',null=True,blank=True,verbose_name='����Ŀ¼',                                   
help_text='�����',related_name='sub_cat',on_delete=models.CASCADE)
    is_tab=models.BooleanField(default=False,verbose_name='�Ƿ񵼺�',help_text='�Ƿ񵼺�')
    class Meta:
        verbose_name='��Ʒ���'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
