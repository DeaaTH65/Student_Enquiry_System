from django.shortcuts import render, redirect
from app_students.models import StudentModel, CourseModel
from app_students.forms import StudentCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login')
def student_create(request):
    form = StudentCreateForm()
    context = {"form": form}

    if request.method == "POST":
        # user = User.objects.get(id=request.user.id)
        # std = StudentCreateForm(request.POST, request.FILES)
        course = CourseModel.objects.get(id=request.POST.get('course'))
        std_obj = StudentModel()
        std_obj.first_name = request.POST.get('first_name')
        std_obj.middle_name = request.POST.get('middle_name')
        std_obj.last_name = request.POST.get('last_name')
        std_obj.email = request.POST.get('email')
        std_obj.contact = request.POST.get('contact')
        std_obj.address = request.POST.get('address')
        std_obj.course = course
        std_obj.current_degree = request.POST.get('current_degree')
        std_obj.profile_img = request.FILES.get('profile_img') # for file from form
        std_obj.user = request.user
        std_obj.save()
        # if std.is_valid():
        #     std.user = user
        #     std.save()
        #     return redirect("student-index")
        return redirect("student-index")
    return render(request, 'students/create.html', context)

@login_required(login_url='/login')
def student_index(request):
    #students = StudentModel.objects.all() #- for all data
    students = StudentModel.objects.filter(user=request.user) # filter by user
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
        std = StudentCreateForm(data=request.POST, instance=student, files=request.FILES)
        if std.is_valid():
            std.save()
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
    return redirect("student-index")