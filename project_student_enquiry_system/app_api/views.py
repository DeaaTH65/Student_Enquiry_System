from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from app_api.serializers import CourseSerializer, StudentSerializer
from app_courses.models import CourseModel
from app_students.models import StudentModel

# Create your views here.
class CourseApiView(APIView):
    def get(self, request):
        course_obj = CourseModel.objects.all()

        # serialing model object
        serializer = CourseSerializer(course_obj)

        # return api response with serialize object
        return Response(serializer.data)

    def post(self, request):
        pass