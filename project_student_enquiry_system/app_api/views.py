from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from app_api.serializers import CourseSerializer, StudentSerializer, UserSerializer
from app_courses.models import CourseModel
from app_students.models import StudentModel
from django.contrib.auth.models import User

# Create your views here.
class CourseApiView(APIView):
    def get(self, request):
        course_obj = CourseModel.objects.all() # queryset
        # serialing model object
        serializer = CourseSerializer(course_obj, many=True)
        # return api response with serialize object
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CourseApiIdView(APIView):
    def get_object(self, id):
        try:
            course_obj = CourseModel.objects.get(id=id)
            return course_obj
        except CourseModel.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)
        if instance is None:
            return Response({"error": "No data found"})
        serializer = CourseSerializer(instance)
        return Response(serializer.data)

    def put(self, request, id):
        instance = self.get_object(id)
        if instance is None:
            return Response({"error": "No data found"})
        
        serializer = CourseSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        instance = self.get_object(id)
        if instance is None:
            return Response({"error": "No data found"})
        instance.delete()
        return Response({"message": "Data deleted successfully"})

class StudentApiView(APIView):
    def get(self, request):
        std_obj = StudentModel.objects.all()
        serializer = StudentSerializer(std_obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)