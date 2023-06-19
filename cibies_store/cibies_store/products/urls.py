from django.urls import path
from cibies_store.products.views import indexx


urlpatterns = [
    path('', indexx, name='index'),
]