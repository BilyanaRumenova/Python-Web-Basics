from django.urls import path

from books_app.books.views import index, create_book, edit_book

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_book, name='create book'),
    path('edit/<int:pk>', edit_book, name='edit book')
]