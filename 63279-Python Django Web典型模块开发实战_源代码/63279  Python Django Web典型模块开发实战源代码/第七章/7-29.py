from django.contrib import admin
from django.urls import path
#�����ȡ�����б���ͼ�࣬��ȡ������ͼ��
from app01.views import GetArticleView,GetCommentView
#�����ȡ��¼��ͼ�࣬��ȡ����������ͼ�࣬����������ͼ��
from app01.views import LoginView,PushArticleView,PushCommentView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',LoginView.as_view(),name='login'),
    path('getarticle/',GetArticleView.as_view(),name='getarticle'),
    path('getcomment/',GetCommentView.as_view(),name='getcomment'),
    path('pusharticle/',PushArticleView.as_view(),name='pusharticle'),
    path('pushcomment/',PushCommentView.as_view(),name='pushcomment')
]
