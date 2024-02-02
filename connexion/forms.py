from django import forms
from django.contrib.auth.forms import UserCreationForm
from stage.models import Utilisateur,Departement

# class UtilisateurCreationForm(forms.Form):

class UtilisateurCreationForm(forms.Form):
    username =forms.CharField(label="username") 
    nom=forms.CharField(label="Nom d'utilisateur")
    password=forms.CharField(label="password")
    prenom=forms.CharField(label="Prenom d'utilisateur")
    email =forms.EmailField(label ='Donner votre email')
    numero_telephone = forms.IntegerField(label="donner votre numero telephone")
    age = forms.IntegerField(label="donner votre age")
    diplome = forms.CharField(label="donner un diplome")
    departement = forms.ModelChoiceField(queryset=Departement.objects.all(), label="Département")