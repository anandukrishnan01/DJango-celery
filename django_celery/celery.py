from __future__ import absolute_import, unicode_literals
import os


from celery import Celery
from celery.schedules import timedelta

# Set default Django settings module for 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

# Create Celery instance
app = Celery('django_celery')

app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
# Load settings from Django settings, CELERY namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# celery_beat_settings
app.conf.beat_schedule = {
    # 'send-mail-periodic': {
    #     'task': 'app1.tasks.send_mail_task',
    #     'schedule': crontab(hour=12,minute=25),
    # },
    # 'send-mail-periodic': {
    #     'task': 'app1.tasks.send_mail_task',
    #     'schedule': timedelta(seconds=10),
    # },
    'print-success-message-every-10-seconds': {
        'task': 'app1.tasks.test_func',
        'schedule': 10.0,  # Every 10 seconds
    }
}

# Load task modules from all registered Django app configs
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
