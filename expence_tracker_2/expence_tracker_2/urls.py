from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expence_tracker_2.expenses_app.urls')),
    path('', include('expence_tracker_2.profile_app.urls')),
]
