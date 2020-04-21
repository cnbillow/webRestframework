REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', #������
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    )
}
import datetime
JWT_AUTH = {
 # ָ��token����Ч��
 'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
}
