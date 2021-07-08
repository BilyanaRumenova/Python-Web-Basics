from django.urls import path

from notes_app.note_app.views import home_page, add_note, edit_note, delete_note, note_details

urlpatterns = [
    path('', home_page, name='home page'),
    path('add/', add_note, name='add note'),
    path('edit/:<int:pk>', edit_note, name='edit note'),
    path('delete/:<int:pk>', delete_note, name='delete note'),
    path('details/:<int:pk>', note_details, name='note details'),
]

