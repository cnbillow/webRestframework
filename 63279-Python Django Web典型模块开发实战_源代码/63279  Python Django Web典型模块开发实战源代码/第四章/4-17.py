INSTALLED_APPS = [
#����
    'app01.apps.App01Config',
    'rest_framework',
    'corsheaders'
]
#......
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',#�ŵ��м������
    'django.middleware.security.SecurityMiddleware',
#����
]
#......
CORS_ORIGIN_ALLOW_ALL = True
