from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('app_courses.urls')),
    path('students/', include('app_students.urls')),
    path('', include('app_accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
