CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache', # ָ������ʹ�õ�����
  'LOCATION': '222.169.10.100:11211',         # ָ��Memcache�����������IP��ַ�Ͷ˿�
  'OPTIONS':{
   'MAX_ENTRIES': 300,            # ��󻺴��¼��������Ĭ��300��
   'CULL_FREQUENCY': 3,           # ���浽��������֮���޳���������ı���������1/CULL_FREQUENCY��Ĭ��3��
  }
 }
}
