from django import forms
from app_students.models import StudentModel

class StudentCreateForm(forms.ModelForm):
    class Meta:
        fields = ("first_name", "middle_name", "last_name", "email", "contact", "address", "course", "current_degree")
        model = StudentModel
