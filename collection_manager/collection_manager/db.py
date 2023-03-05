LOCAL = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'tinku',
            'USER': 'admin',
            'PASSWORD': 'k2JgeRF#FBJK=bTJ',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }

GAE = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=tinku'
        },
        'NAME': 'general',
        'USER': 'admin',
        'PASSWORD': 'k2JgeRF#FBJK=bTJ',
        'PORT': '5432'
    }
}
