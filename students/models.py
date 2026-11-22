from django.db import models

class Student(models.Model):
    ine= models.CharField(max_length=10)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_naissance=models.DateField()
    createdat=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
class Inscription(models.Model):
    date_inscription=models.DateField()
    montant_inscription =models.FloatField()
    Student =models.ForeignKey(Student,on_delete=models.CASCADE)
