import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News_Portal_app.settings')

app = Celery('News_Portal_app')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()