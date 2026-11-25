from django.shortcuts import render
 
from .models import Teacher
 
 
def teacher_list(request):
    context = {"teachers": Teacher.objects.all()}
    return render(request, "teachers/teacher_list.html", context)

