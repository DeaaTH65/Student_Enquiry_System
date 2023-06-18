from django.db import models
from app_courses.models import CourseModel
from django.contrib.auth.models import User

# Create your models here.
class StudentModel(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)
    address =  models.CharField(max_length=200)
    current_degree = models.CharField(max_length=200)
    profile_img = models.FileField(upload_to='students/profiles/', null=True, blank=True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'tbl_students'