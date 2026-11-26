from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "email",
            "classe",
            "phone",
            "birth_date",
            "active",
        ]
        def clean_phone(self): 
            phone = self.cleaned_data["phone"].replace(" ", "") 
            if phone and (not phone.isascii() or 
                      not phone.isdigit() or len(phone) != 9): 
                raise forms.ValidationError("Saisir 9 chiffres.") 
            return phone 