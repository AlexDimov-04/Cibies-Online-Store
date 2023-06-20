from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from cibies_store.user_profile.validators import alphanumeric_charcters_validator, first_letter_uppercase_validator

class Profile(models.Model):
    MAX_LENGTH_NAME = 35
    MIN_LENGTH_NAME = 2
    MAX_LENGTH_EMAIL = 40
    MAX_LENGTH_PASSWORD = 20
    MIN_LENGTH_PASSWORD = 6
    MIN_AGE_RESTRICTION = 16

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=[
            MinLengthValidator(MIN_LENGTH_NAME),
            alphanumeric_charcters_validator,
            first_letter_uppercase_validator
        ],
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=[
            MinLengthValidator(MIN_LENGTH_NAME),
            alphanumeric_charcters_validator,
            first_letter_uppercase_validator
        ]
    )

    email = models.EmailField(
        max_length=MAX_LENGTH_EMAIL,
    )

    password = models.CharField(
        max_length=MAX_LENGTH_PASSWORD,
        validators=[MinLengthValidator(MIN_LENGTH_PASSWORD)]
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(MIN_AGE_RESTRICTION)]
    )
    