CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # ָ������ʹ�õ�����
  'LOCATION': 'unique-snowflake',         # д���ڴ��еı�����Ψһֵ 
  'TIMEOUT':300,             # ���泬ʱʱ��(Ĭ��Ϊ300��,None��ʾ��������)
  'OPTIONS':{
   'MAX_ENTRIES': 300,           # ��󻺴��¼��������Ĭ��300��
   'CULL_FREQUENCY': 3,          # ���浽��������֮���޳���������ı���������1/CULL_FREQUENCY��Ĭ��3��
  }  
 }
}
