
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("<h1>Bienvenue dans notre école</h1>")


def student_list(request):
    return HttpResponse("<h1>Liste des étudiants</h1>")


def student_detail(request, id):
    return HttpResponse(f"<h1>Détails de l'étudiant {id}</h1>")


def teachers(request):
    return HttpResponse("<h1>Liste des enseignants</h1>")


def courses(request):
    return HttpResponse("<h1>Liste des cours</h1>")


def about(request):
    return HttpResponse("<h1>Présentation de notre école</h1>")


    
# Create your views here.
