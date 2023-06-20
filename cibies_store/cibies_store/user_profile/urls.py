from django.urls import path, include
from cibies_store.user_profile.views import index \
    ,create_profile, details_profile, delete_profile, edit_profile

profile_patterns = [
    path('create/', create_profile, name='create profile'),
    path('details/', details_profile, name='details profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
]

urlpatterns = [
    path('', index, name='index'),
    path('profile/', include(profile_patterns))
]