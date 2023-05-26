from django.db import models

# Create your models here.
class CourseModel(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name + " - " + self.course_code

    class Meta:
        db_table = "tbl_courses"
