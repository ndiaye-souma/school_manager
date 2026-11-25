from django.http import Http404, HttpResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Student

STUDENTS = [
{"id": 1, "first_name": "Awa", "last_name": "Diop", "classe": "L1", "active": True},
{"id": 2, "first_name": "Moussa", "last_name": "Fall", "classe": "L2", "active": True},
{"id": 3, "first_name": "Fatou", "last_name": "Ndiaye", "classe": "L1", "active": False},
{"id": 4, "first_name": "Ibrahima", "last_name": "Sow", "classe": "L3", "active": True},
]

def student_list(request):
    query = request.GET.get("q", "")
    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    context = {
        "students": students,
        "query": query
    }

    return render(request, "students/student_list.html", context)
    return render(request, "students/student_list.html", context)

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    context = {"student": student}
    return render(request, "students/student_detail.html", context)

def students_by_class(request, classe):
    students = Student.objects.filter(classe=classe)
    context = {"students": students}
    return render(request, "students/student_list.html", context)

