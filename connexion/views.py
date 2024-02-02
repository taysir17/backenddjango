from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from connexion.forms import UtilisateurCreationForm
from django.contrib.auth.models import User
from stage.models import Utilisateur

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('stage:index')
        else:
            messages.error(request, 'Identifiant ou mot de passe incorrect')
    else:
        form = AuthenticationForm()
        return render(request, 'connexion/login.html', {"form": form})

def logout_user(request):
    logout(request)
    return redirect('stage:index')

def register_user(request): 
    if request.method == 'POST':
        form =UtilisateurCreationForm(request.POST)

        if form.is_valid():
                # Access form field values from cleaned_data
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = User.objects.create_user(username,password)
                # 
                email = form.cleaned_data["email"]
                nom = form.cleaned_data["nom"]
                prenom = form.cleaned_data["prenom"]
                numero_telephone = form.cleaned_data["numero_telephone"]
                age = form.cleaned_data["age"]
                diplome = form.cleaned_data["diplome"]
                departement = form.cleaned_data["departement"]
                
                Utilisateur.objects.create(
                    nom=nom,
                    prenom=prenom,
                    email=email,
                    numero_telephone=numero_telephone,
                    age=age,
                    diplome=diplome,
                    departement=departement,
                    user=user
                )
                return redirect('connexion/login.html')
        else:
            form = UtilisateurCreationForm()
            return render(request, 'connexion/register.html',{"form":form})
    else:
        form = UtilisateurCreationForm()
        return render(request, 'connexion/register.html',{"form":form})