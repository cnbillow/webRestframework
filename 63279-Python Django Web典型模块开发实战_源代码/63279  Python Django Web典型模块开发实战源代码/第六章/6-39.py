from django.contrib import admin
from django.urls import path
#������ص���ͼ��
from app01.views import AuthView,CommonVideoView,VIPVideoView,SVIPVideoView
urlpatterns = [
path('admin/', admin.site.urls),
#��¼��֤
path('auth/',AuthView.as_view(),name='auth'),
#��ȡ��ͨ��Դ
path('common/',CommonVideoView.as_view(),name='common'),
#��ȡVIP��Դ
path('vip/',VIPVideoView.as_view(),name='vip'),
#��ȡSVIP��Դ
    path('svip/',SVIPVideoView.as_view(),name='svip'),
]
