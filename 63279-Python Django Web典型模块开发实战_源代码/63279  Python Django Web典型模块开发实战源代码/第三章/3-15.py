MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',#�ŵ��м������
    'Django.middleware.security.SecurityMiddleware',
    'Django.contrib.sessions.middleware.SessionMiddleware',
    'Django.middleware.common.CommonMiddleware',
    'Django.middleware.csrf.CsrfViewMiddleware',
    'Django.contrib.auth.middleware.AuthenticationMiddleware',
    'Django.contrib.messages.middleware.MessageMiddleware',
    'Django.middleware.clickjacking.XFrameOptionsMiddleware',
]
