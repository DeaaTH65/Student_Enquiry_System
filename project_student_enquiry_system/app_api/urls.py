from django.urls import path
from app_api.views import CourseApiView, StudentApiView, CourseApiIdView

urlpatterns = [
    path('courses/', CourseApiView.as_view()),
    path('courses/<int:id>/', CourseApiIdView.as_view()),
    path('students/', StudentApiView.as_view())
]