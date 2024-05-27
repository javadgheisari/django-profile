# output.py
import os    
def get_wsgi_application(*args, **kwargs):  
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")
    from django.core.wsgi import get_wsgi_application
    return get_wsgi_application(*args, **kwargs)

