# coding=utf-8
DATABASES_CONFIG = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'sigesic',
       'USER': 'postgres',
       'PASSWORD': 'admin8080',
       'HOST': 'localhost',
       'PORT': '5432',
      'ATOMIC_REQUESTS': True, # Crea transacciones en cada petición de la vista
  }
}