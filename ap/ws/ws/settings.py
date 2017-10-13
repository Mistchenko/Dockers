import os
from logging.handlers import SysLogHandler

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'k0zg0kibq7lv3$vcodk0*6g&nq8yzgue_wfxvai%k1yy@5=myd'
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0']


# Application definition

INSTALLED_APPS = (
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    # 'django.contrib.staticfiles',
    'app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ws.urls'
WSGI_APPLICATION = 'ws.wsgi.application'

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'

# ---------------------------------------------------------------------------------------------
HOST_NAME = 'dev'
WS_LOG_FORMAT = '{0}:[%(asctime)s] - %(levelname)s - %(message)s'.format(HOST_NAME)
PING_LOG_FORMAT = '{0}:[%(asctime)s] - %(message)s'.format(HOST_NAME)
LOG_DATE_FORMAT = '%a %b %d %H:%M:%S %Y'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'rootFormatter': {
            'format': WS_LOG_FORMAT,
            'datefmt': LOG_DATE_FORMAT,
        },
        'pingFormatter': {
            'format': PING_LOG_FORMAT,
            'datefmt': LOG_DATE_FORMAT,
        },
        'samlFormatter': {
            'format': WS_LOG_FORMAT,
            'datefmt': LOG_DATE_FORMAT,
        },
    },
    'handlers': {
        'rootHandler': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'formatter': 'rootFormatter',
            'facility': SysLogHandler.LOG_LOCAL2,
        },
        'pingHandler': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'formatter': 'pingFormatter',
            'facility': SysLogHandler.LOG_LOCAL3,
        },
        'samlHandler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'formatter': 'samlFormatter',
            'facility': SysLogHandler.LOG_LOCAL6,
        },
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        }
    },
    'loggers': {
        '': {
            'handlers': ['rootHandler'],
            'level': 'INFO',
            'propagate': True,
        },
        'ping': {
            'handlers': ['pingHandler'],
            'level': 'INFO',
            'propagate': False,
        },
        'saml': {
            'handlers': ['samlHandler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'djangosaml2': {
            'handlers': ['samlHandler'],
            'level': 'DEBUG',
        },
        'saml2': {
            'handlers': ['samlHandler'],
            'level': 'DEBUG',
        },
        'factory': {
            'level': 'ERROR',
            'propagate': False
        }
    }
}

LOG_TEMPLATES = {"GENERAL": "Service:'{service}' Reply:'{code}' Time:'{response_time}' StartTime:'{start_time}' ClientID:'{client_id}' Request:'{parameters}'",
                 "LOGIN": "Service:'{service}' Report: session with SID='{sid}' opened for user with UID='{uid}',LDAP_UID='{ldap_uid}',DisplayName='{display_name}',Host='%s'" % HOST_NAME,
                 "CUSTOMER": "Service:'{service}' Report: Customer='{customer}',SID='{sid}'",
                 "REPORT": "Service:'{service}' basefilename: {filename} fullpath: {path}",
                 "DOWNLOAD": "Service:'{service}' Report: UID='{ldap_uid}' downloaded {type} files, filename='{filename}'",
                 "TABLEAU": "Service:'{service}' Report: UID='{ldap_uid}', tableau url='{url}'",
                 "ERROR": "Service:'{service}' [{code}] {message} Details: '{details}'",
                 "LDAP": "Message:'using '{server}' ldap server'",
                 "PING": "Report: Host={host},Customer={customer},SID={sid},LDAP_UID={ldap_uid},info={info}",
                 "SEARCH": "Message: sphinx found non-existing claims: {claims}",
                 "CLIENT_ID": "Message: client ID '{client_id}' does not match the expected format"}
