# ����redis����
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # ���redis server���������룬��д�� "LOCATION": "����@redis://127.0.0.1:6379",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
