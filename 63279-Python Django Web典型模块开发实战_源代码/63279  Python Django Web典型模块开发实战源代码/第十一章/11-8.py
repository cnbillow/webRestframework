CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.dummy.DummyCache',  # �����̨ʹ�õ�����
  'TIMEOUT': 300,            # ���泬ʱʱ�䣨Ĭ��300�룬None��ʾ�������ڣ�0��ʾ�������ڣ�
  'OPTIONS':{
   'MAX_ENTRIES': 300,          # ��󻺴��¼��������Ĭ��300��
   'CULL_FREQUENCY': 3,          # ���浽��������֮���޳���������ı���������1/CULL_FREQUENCY��Ĭ��3��
  },
 }
}
