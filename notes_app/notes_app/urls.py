from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes_app.note_app.urls')),
    path('', include('notes_app.profile_app.urls')),
]
