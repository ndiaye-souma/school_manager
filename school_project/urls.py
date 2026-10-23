"""
URL configuration for school_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from students.views import (home,   
    student_list,
    student_detail,
    students_by_class,
    teacher_list,
    about)
def teachers(request):
     return HttpResponse("<h1>Liste des enseignants</h1>") 
def courses(request):
     return HttpResponse("<h1>Liste des cours</h1>") 
def about(request): 
    return HttpResponse("<h1>Présentation de notre école</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('students/', student_list, name='student_list'),
    path('students/<int:id>/', student_detail, name='student_detail'),
    path('teachers/', teacher_list, name='teacher_list'), 
    path('courses/', courses, name='courses'),
    path('about/', about, name='about'),
    path('students/classe/<str:classe>/', students_by_class, 
     name='students_by_class'), 
]