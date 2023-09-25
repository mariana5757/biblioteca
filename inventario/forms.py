from django import forms
from .models import User

class Create_loan(forms.Form):
    AVAILABLE_USER_IDS =  [(User.id, f'{User.full_name}') for User in User.objects.all()]
    user_id = forms.ChoiceField(label = "user: ", choices=AVAILABLE_USER_IDS)
    loan_date = forms.DateField(label= "fecha de prestamo: ")
    due_date = forms.DateField(label= "fecha de devolución: ")

class Create_user(forms.Form):
    full_name = forms.CharField(label= "Nombre")
    email = forms.CharField(label= "Email")
    apellido = forms.IntegerField(label = "Apellido")

class Create_book(forms.Form):
    name = forms.CharField(label = "Titulo del libro: ")
    author = forms.CharField(label = "Autor del libro: ")
    units = forms.IntegerField(label ="Unidades disponibles: ")