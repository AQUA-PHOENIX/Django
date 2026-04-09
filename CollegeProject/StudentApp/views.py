from django.shortcuts import render
from .models import Student
# Create your views here.
def student_list(request):
    student = Student.objects.all()
    return render(request, 'Student_App/student_list.html',{
        'students' : student
    })

