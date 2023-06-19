from rest_framework import serializers
from app_courses.models import CourseModel
from app_students.models import StudentModel

class CourseSerializer(serializers.Serializer):
    class Meta:
        fields = ("course_name", "course_code")
        model = CourseModel
        
class StudentSerializer(serializers.Serializer):
    class Meta:
        fields = ("first_name", "middle_name", "last_name", "email", "contact", "address", "course", "current_degree", "profile_img")
        model = StudentModel