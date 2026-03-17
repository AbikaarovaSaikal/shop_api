from rest_framework.exceptions import ValidationError
from datetime import datetime


def validate_user_age(request):
    birthdate = request.auth.get("birthdate")

    if not birthdate:
        raise ValidationError(
            "У вас не указана дата рождения!"
        )

    birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()

    today = datetime.today().date()
    age = today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day)
    )

    if age < 18:
        raise ValidationError(
            "Создавать продукты могут только лица достигшие 18 лет!"
        )