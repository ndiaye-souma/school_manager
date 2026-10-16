from django.shortcuts import render
from django.http import HttpResponse

 
def home(request):
    return HttpResponse("Bienvenue dans School Manager")

def  student_list(request):
    return HttpResponse("Liste des étudiants")

def student_detail(request, id):
    return HttpResponse(f"Détail de l'étudiant {id}")
# Create your views here.
