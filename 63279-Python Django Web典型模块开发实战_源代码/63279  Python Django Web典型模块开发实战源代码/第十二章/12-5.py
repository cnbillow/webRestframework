DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '12a',
        'USER':'root',
        'PASSWORD':'mysql����',
        'HOST':'127.0.0.1',
        "OPTIONS":{"init_command":"SET default_storage_engine=INNODB;"}#��������¼���ܱ������
    }
}
