from django.db import models
from cibies_store.user_profile.models import Profile
from cibies_store.user_profile.validators import alphanumeric_charcters_validator
from django.core.validators import MinLengthValidator

class Product(models.Model):
    MAX_LENGTH_PRODUCT_NAME = 30

    name = models.CharField(
        max_length=MAX_LENGTH_PRODUCT_NAME,
        validators=[MinLengthValidator, alphanumeric_charcters_validator]
    )

    image_url = models.URLField()

    description = models.TextField()

    weight = models.IntegerField(
        null=True,
        blank=True,
    )