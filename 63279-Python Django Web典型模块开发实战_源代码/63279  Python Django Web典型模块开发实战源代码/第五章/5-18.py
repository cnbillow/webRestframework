from rest_framework.authtoken import views
urlpatterns = [
    #����
#drf�Դ���token��֤ģʽ
    path('api-token-auth/', views.obtain_auth_token),
]
