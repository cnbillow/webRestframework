CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.db.DatabaseCache',  # ָ������ʹ�õ�����
  'LOCATION': 'cache_table',          # ���ݿ��    
  'OPTIONS':{
   'MAX_ENTRIES': 300,           # ��󻺴��¼��������Ĭ��300��
   'CULL_FREQUENCY': 3,          # ���浽��������֮���޳���������ı���������1/CULL_FREQUENCY��Ĭ��3��
  }  
 }   
}
