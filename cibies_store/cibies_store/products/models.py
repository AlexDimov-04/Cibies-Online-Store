from django.db import models
from cibies_store.user_profile.validators import alphanumeric_charcters_validator
from django.core.validators import MinLengthValidator, MinValueValidator

class Product(models.Model):
    MAX_LENGTH_PRODUCT_NAME = 30
    MIN_VALUE_PRICE = 1
    MIN_VALUE_WEIGHT = 0.1

    name = models.CharField(
        max_length=MAX_LENGTH_PRODUCT_NAME,
        validators=[MinLengthValidator, alphanumeric_charcters_validator]
    )

    image_url = models.URLField()

    description = models.TextField()

    price = models.FloatField(
        validators=[MinValueValidator(MIN_VALUE_PRICE)],
        default=''
    )

    weight = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(MIN_VALUE_WEIGHT)]
    )