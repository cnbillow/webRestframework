from django.contrib import admin
from django.urls import path
#����ģ�����������ͼ��
from app01.views import GetArticleViews
urlpatterns = [
path('admin/', admin.site.urls),
#��������·��
    path('getlist/',GetArticleViews.as_view(),name='getlist'),
]
