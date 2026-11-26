from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Student
from django.shortcuts import redirect
from django.contrib import messages
from .forms import StudentForm 


# Liste des étudiants avec recherche
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


# Détail d'un étudiant
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    context = {
        "student": student
    }

    return render(request, "students/student_detail.html", context)


# Filtrer les étudiants par classe
def students_by_class(request, classe):
    students = Student.objects.filter(classe=classe)

    context = {
        "students": students
    }

    return render(request, "students/student_list.html", context)


# Ajouter un étudiant
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save()
            messages.success(request, "Étudiant ajouté avec succès.")
            return redirect("students:detail", id=student.id)

    else:
        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {"form": form, "title": "Ajouter un étudiant"}
    )



def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, "Étudiant modifié avec succès.")
            return redirect("students:detail", id=student.id)

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "students/student_form.html",
        {"form": form, "title": "Modifier un étudiant"}
    )


# Supprimer un étudiant
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        name = str(student)
        student.delete()

        messages.success(
            request,
            f"{name} a été supprimé avec succès."
        )

        return redirect("students:list")

    context = {
        "student": student
    }

    return render(
        request,
        "students/student_confirm_delete.html",
        context
    )
