from django.urls import path

from templates_advanced.pythons_auth import views

urlpatterns = (
    path('sign-in/', views.sign_in, name='sign in'),
    path('sign-out/', views.sign_out, name='sign out'),
    path('sign-up/', views.sign_up, name='sign up'),
)