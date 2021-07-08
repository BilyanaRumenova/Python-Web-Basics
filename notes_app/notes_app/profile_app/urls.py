from django.urls import path

from notes_app.profile_app.views import profile_details, delete_profile

urlpatterns = [
    path('profile/', profile_details, name='profile details'),
    path('profile/delete', delete_profile, name='delete profile'),
]


