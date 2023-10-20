from django.urls import path
from . import views

urlpatterns = [
    path('student_course_list/', views.student_course_list, name='student_course_list'),
    path('', views.student_course_list, name='home'),
]
