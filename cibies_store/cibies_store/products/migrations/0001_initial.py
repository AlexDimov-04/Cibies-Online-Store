# Generated by Django 4.2.2 on 2023-06-19 16:25

import cibies_store.user_profile.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator, cibies_store.user_profile.validators.alphanumeric_charcters_validator])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('weight', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
