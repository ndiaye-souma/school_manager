from django.shortcuts import render
 
 
def home(request):
    context = {
        "school_name": "Lycée d'Excellence de Dakar",
        "nb_classes": 12,
    }
    return render(request, "pages/home.html", context)
 
 
def about(request):
    return render(request, "pages/about.html")
