from .base import *

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_LOCAL_ENGINE'),
        'NAME': os.getenv('DB_LOCAL_NAME'),
    }
}