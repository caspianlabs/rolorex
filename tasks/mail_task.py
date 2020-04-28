from django.conf import settings
from django.core.mail import send_mail, mail_admins
from django.template import Engine, Context

from rolorex.celery import app


def render_template(template, context):
    engine = Engine.get_default()
    tmpl = engine.get_template(template)
    return tmpl.render(Context(context))


@app.task
def send_email_task(recipients, subject, template, context):
    send_mail(
        subject=subject,
        message=render_template(f'{template}.txt', context),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipients,
        fail_silently=False
    )


@app.task
def mail_admins_task(subject, template, context):
    mail_admins(
        subject=subject,
        message=render_template(f'{template}.txt', context),
        fail_silently=False
    )
