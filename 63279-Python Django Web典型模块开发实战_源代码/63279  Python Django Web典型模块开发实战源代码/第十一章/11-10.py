CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache', #ָ������ʹ�õ�����
  'LOCATION': '/var/tmp/django_cache',        #ָ�������·��
  'TIMEOUT':300,              #���泬ʱʱ��(Ĭ��Ϊ300��,None��ʾ��������)
  'OPTIONS':{
   'MAX_ENTRIES': 300,            # ��󻺴��¼��������Ĭ��300��
   'CULL_FREQUENCY': 3,           # ���浽��������֮���޳���������ı���������1/CULL_FREQUENCY��Ĭ��3��
  }
 }   
}
