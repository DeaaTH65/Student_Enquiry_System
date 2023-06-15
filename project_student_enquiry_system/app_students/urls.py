from django.urls import path
from . import  views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', views.student_index, name='student-index'),
    path('create/', views.student_create, name='student-create'),
    path('edit/<int:id>/', views.student_edit, name='student-edit'),
    path('show/<int:id>/', views.student_show, name='student-show'),
    path('delete/<int:id>/', views.student_delete, name='student-delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    