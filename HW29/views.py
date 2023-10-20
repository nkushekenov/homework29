from django.shortcuts import render
from .models import Student, Course

def student_course_list(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'HW29/student_course_list.html', {'students': students, 'courses': courses})
