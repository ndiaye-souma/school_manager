from django.http import Http404, HttpResponse
from django.shortcuts import render

STUDENTS = [
{"id": 1, "first_name": "Awa", "last_name": "Diop", "classe": "L1", "active": True},
{"id": 2, "first_name": "Moussa", "last_name": "Fall", "classe": "L2", "active": True},
{"id": 3, "first_name": "Fatou", "last_name": "Ndiaye", "classe": "L1", "active": False},
{"id": 4, "first_name": "Ibrahima", "last_name": "Sow", "classe": "L3", "active": True},
]

TEACHERS = [
{"first_name": "Mamadou", "last_name": "Ba", "subject": "Mathématiques"},
{"first_name": "Aïssatou", "last_name": "Sy", "subject": "Informatique"},
{"first_name": "Cheikh", "last_name": "Diallo", "subject": "Anglais"},
]

def home(request):
    return render(request, "students/home.html")

def student_list(request):
    context = {"students": STUDENTS}
    return render(request, "students/student_list.html", context)

def student_detail(request, id):
    for student in STUDENTS:
        if student["id"] == id:
            context = {"student": student}
    return render(request, "students/student_detail.html", context)



def teacher_list(request):
    context = {"teachers": TEACHERS}
    return render(request, "students/teachers.html", context)

def students_by_class(request):
    return render(request, "students/students_by_class.html")

def courses(request):
    return HttpResponse("<h1>Liste des cours</h1>")

def about(request):
    return render(request, "students/about.html")


