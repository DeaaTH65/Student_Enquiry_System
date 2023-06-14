from django.shortcuts import render, redirect
from app_students.models import StudentModel
from app_students.forms import StudentCreateForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def student_create(request):
    form = StudentCreateForm()
    context = {"form": form}

    if request.method == "POST":
        std = StudentCreateForm(request.POST)
        if std.is_valid():
            std.save()
            messages.success(request, "Data added successfully")
            return redirect("student-index")
        return redirect("student-create")
    return render(request, 'students/create.html', context)


@login_required(login_url='/login')
def student_index(request):
    students = StudentModel.objects.all()
    context = {
        "students" : students, 
        "title": "SES | Student List", 
        "body_title": "Here are the students list"
        }
    return render(request, "students/index.html", context)

@login_required(login_url='/login')
def student_edit(request, id):
    student = StudentModel.objects.get(id=id)
    form = StudentCreateForm(instance=student)
    context = {"form": form}
    if request.method == "POST":
        std = StudentCreateForm(data=request.POST, instance=student)
        if std.is_valid():
            std.save()
            messages.success(request, "Data updated successfully")
            return redirect("student-index")
        return redirect("student-edit", id)
    return render(request, 'students/edit.html', context)


@login_required(login_url='/login')
def student_show(request, id):
    student = StudentModel.objects.get(id=id)
    context = {"student": student}
    return render(request, 'students/show.html', context)


@login_required(login_url='/login')
def student_delete(request, id):
    student = StudentModel.objects.get(id=id)
    student.delete()
    messages.success(request, "Data deleted successfully")
    return redirect("student-index")
