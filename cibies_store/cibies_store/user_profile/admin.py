from django.contrib import admin
from cibies_store.user_profile.models import Profile
from cibies_store.products.models import Product

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

