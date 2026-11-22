from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Student

STUDENTS = [
{"id": 1, "first_name": "Awa", "last_name": "Diop", "classe": "L1", "active": True},
{"id": 2, "first_name": "Moussa", "last_name": "Fall", "classe": "L2", "active": True},
{"id": 3, "first_name": "Fatou", "last_name": "Ndiaye", "classe": "L1", "active": False},
{"id": 4, "first_name": "Ibrahima", "last_name": "Sow", "classe": "L3", "active": True},
]

def student_list(request):
    students =students.objects.all()
    context = {"students": students }
    return render(request, "students/student_list.html", context)


def student_detail(request, id):
    for student in STUDENTS:
        if student["id"] == id:
            context = {"student": student}
            return render(request, "students/student_detail.html", context)
def students_by_class(request, classe):
    students = [
        student for student in STUDENTS
        if student["classe"] == classe
    ]

    return render(request, "students/student_list.html", {
        "students": students,
        "classe": classe
    })