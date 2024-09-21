from celery import shared_task
from django.core.mail import send_mail as django_send_mail
from django.contrib.auth import get_user_model
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


@shared_task(blind=True)
def test_func():
    logger.info("Success! The task was executed.")
    print("Success! The task was executed.")
    return "Done"


@shared_task
def send_mail_task():
    # Your task code here
    pass
# @shared_task(bind=True)
# def send_mail_task(self):
#     users = get_user_model().objects.all()
#     logger.info("Fetching users: %s", users)
#     for user in users:
#         mail_subject = "Celery Test"
#         message = "Is it working?"
#         to_email = user.email
#         try:
#             django_send_mail(
#                 subject=mail_subject,
#                 message=message,
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[to_email],
#                 fail_silently=False,  # Changed to False to catch errors
#             )
#             logger.info("Email sent to: %s", user.email)
#         except Exception as e:
#             logger.error("Failed to send email to %s: %s", user.email, str(e))
#     return "Done"
