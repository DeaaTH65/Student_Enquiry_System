from django.urls import path
from app_api.views import CourseApiView

urlpatterns = [
    path('courses/', CourseApiView.as_view()),
]