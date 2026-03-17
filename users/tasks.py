from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import random
from datetime import datetime
@shared_task
def random_number():
    number = random.randint(1, 100)
    result = number * 2
    print(f"Случайное число: {number}, результат: {result}")
    return "OK"

@shared_task
def clear_old_data():
    now = datetime.now()
    print(f"Удаляем данные на сегодня {now}")
    return "Данные удалены!"

@shared_task
def remind_about_cart():
    send_mail(
            "Напоминание о корзине",
            "У вас есть товары в корзине. Не забудьте завершить покупку!",
            settings.EMAIL_HOST_USER,
            ["sajkalabdikaarova@gmail.com"],
            fail_silently=False,
        )
    print("Отправляем напоминание")
    return "Напоминания отправлены!"


@shared_task
def send_otp_email(email, code):
    send_mail(
        "Привет новый пользователь!",
        f"Вот твой одноразовый код {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return "CODE SENT"

@shared_task
def todo_homework():
    send_mail(
        "Привет друг",
        "Пора делать домашку",
        settings.EMAIL_HOST_USER,
        ["sajkalabdikaarova@gmail.com"],
        fail_silently=False,
    )
    return "BOLDU"