from django.urls import path

from expence_tracker_2.profile_app.views import home_profile, edit_profile, delete_profile

urlpatterns = [
    path('profile/', home_profile, name='home profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete', delete_profile, name='delete profile')
]
