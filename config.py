from decouple import config
import os
# basedir = os.path.abspath(os.path.dirname(__file__))


# class Config(object):
#     DEBUG = False
#     TESTING = False
#     CSRF_ENABLED = True
#     SECRET_KEY = 'this-really-needs-to-be-changed'
#     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


# class DevelopmentConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True


DB_DETAILS = {
    'dev': {
        'DB_TYPE': 'mysql',
        'DB_NAME': '',
        'DB_HOST': '',
        'DB_NAME': '',
        'DB_USER': '',
        'DB_PASS': ''
    },
    'source': {
        'DB_TYPE': 'postgres',
        'DB_NAME': config('DB_DATABASE_NAME'),
        'DB_HOST': config('DB_HOST'),
        'DB_USER': config('DB_USERNAME'),
        'DB_PASS': config('DB_PASSWORD'),

    },
    'target': {
        'DB_NAME': config('DB_TARGET'),
        'DB_HOST': config('DB_HOST'),
        'DB_PORT': config('DB_PORT'),
        'DB_USER': config('DB_USERNAME'),
        'DB_PASS': config('DB_PASSWORD')
    },
}
