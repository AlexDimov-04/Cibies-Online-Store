from django.urls import path
from cibies_store.user_profile.views import index


urlpatterns = [
    path('', index, name='index'),
]