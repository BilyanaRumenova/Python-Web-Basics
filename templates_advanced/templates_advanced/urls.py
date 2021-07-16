from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('templates_advanced.pythons_app.urls')),
    path('auth/', include('templates_advanced.pythons_auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
