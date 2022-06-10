from django.db.models.signals import post_save, m2m_changed
from django.template.loader import render_to_string
from django.dispatch import receiver
from .models import Post
from django.core.mail import EmailMultiAlternatives
import datetime


@receiver(m2m_changed,  sender=Post.PostCategories.through)
def send_mail(sender, instance, action, **kwargs):
    if action == 'post_add':
        html_content = render_to_string('message.html', {'post': instance})
        category = instance.category.all()
        email = set()
        for cat in category:
            email |= cat.get.email()
        message = EmailMultiAlternatives(
            subject=f'Привет, новый список статей на этой неделе!',
            body=instance.text,
            from_email='c89andrey@yandex.ru',
            to=email,
        )
        message.attach_alternative(html_content, "text/html")

        message.send()


@receiver(post_save, sender=Post)
def check_post(sender, instance, **kwargs):
    today_post = Post.objects.filter(DateCreation=datetime.datetime.now().date())
    return len(today_post)
