from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import TeacherForm
from .models import Teacher


def teacher_list(request):
    context = {"teachers": Teacher.objects.all()}
    return render(request, "teachers/teacher_list.html", context)


def teacher_create(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)

        if form.is_valid():
            teacher = form.save()
            messages.success(request, f"{teacher} a été ajouté(e).")
            return redirect("teachers:list")
    else:
        form = TeacherForm()

    context = {
        "form": form,
        "title": "Ajouter un enseignant"
    }

    return render(request, "teachers/teacher_form.html", context)