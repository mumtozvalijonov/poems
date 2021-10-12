from celery import task
from django.core.mail import send_mail
from django.conf import settings


@task
def send_email_on_registration():
    send_mail(
        'LESSON DJANGO EMAIL',
        'This message has been generated during the lesson',
        settings.EMAIL_HOST_USER,
        ['mumtoz@petricore.tech']
    )
