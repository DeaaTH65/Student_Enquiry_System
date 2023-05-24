from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.course_index, name='course-index'),
    path('create/', views.course_create, name='course-create'),
    path('update/', views.course_update, name='course-update'),
    path('edit/<int:id>/', views.course_edit, name='course-edit'),
    path('show/<int:id>/', views.course_show, name='course-show'),
    path('delete/<int:id>/', views.course_delete, name='course-delete')
]