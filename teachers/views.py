TEACHERS = [
{"first_name": "Mamadou", "last_name": "Ba", "subject": "Mathématiques"},
{"first_name": "Aïssatou", "last_name": "Sy", "subject": "Informatique"},
{"first_name": "Cheikh", "last_name": "Diallo", "subject": "Anglais"},
]

from django.shortcuts import render
 
# Données temporaires : elles iront dans la base à l'étape 13
TEACHERS = [
    {"first_name": "Mamadou", "last_name": "Ba",
     "subject": "Mathématiques"},
    {"first_name": "Aïssatou", "last_name": "Sy",
     "subject": "Informatique"},
    {"first_name": "Cheikh", "last_name": "Diallo",
     "subject": "Anglais"},
]
 
 
def teacher_list(request):
    context = {"teachers": TEACHERS}
    return render(request, "teachers/teacher_list.html", context)

