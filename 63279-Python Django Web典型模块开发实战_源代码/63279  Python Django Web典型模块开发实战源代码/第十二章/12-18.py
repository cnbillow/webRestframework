from django.contrib import admin
from django.urls import path
#����ý���ļ�·��
from django.views.static import serve
from demo12a.settings import MEDIA_ROOT
#��ȡͼ����Ϣ����ͼ��
from app01.views import GetTuWenView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path('getdata/',GetTuWenView.as_view())
]
