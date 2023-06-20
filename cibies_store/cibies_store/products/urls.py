from django.urls import path, include
from cibies_store.products.views import shopping_cart, create_product, delete_product, details_product, edit_product

products_patterns = [
    path('details/', details_product, name='details product'),
    path('edit/', edit_product, name='edit product'),
    path('delete/', delete_product, name='delete product')
]

urlpatterns = [
    path('create-product/', create_product, name='create product'),
    path('shopping-cart/', shopping_cart, name='shopping cart'),
    path('<int:pk>/', include(products_patterns))
]