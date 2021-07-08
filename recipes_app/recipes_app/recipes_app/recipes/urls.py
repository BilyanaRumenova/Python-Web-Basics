from django.urls import path

from recipes_app.recipes.views import home_page, create_recipe, edit_recipe, delete_recipe, details_recipe

urlpatterns = [
    path('', home_page, name='home page'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/:<int:pk>', edit_recipe, name='edit recipe'),
    path('delete/:<int:pk>', delete_recipe, name='delete recipe'),
    path('details/:<int:pk>', details_recipe, name='details recipe'),
    path('details/edit/:<int:pk>', edit_recipe, name='edit recipe'),
    path('details/delete/:<int:pk>', delete_recipe, name='delete recipe'),
]
