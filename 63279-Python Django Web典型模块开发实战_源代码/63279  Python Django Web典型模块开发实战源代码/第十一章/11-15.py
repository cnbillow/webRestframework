CACHES = {
  'default': {
   'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',  # ָ������ʹ�õ�����
   'LOCATION':'192.168.10.100:11211',         # ָ��������11211�˿�ΪMemcache���������
   'OPTIONS':{
    'MAX_ENTRIES': 300,            # ��󻺴��¼��������Ĭ��300��
    'CULL_FREQUENCY': 3,           # ���浽��������֮���޳���������ı���������1/CULL_FREQUENCY��Ĭ��3��
   },  
  }
 }
