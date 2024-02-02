from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Evenement
# Create your views here.

def index(request):
   if request.method == "GET":
      if request.user.is_authenticated:
         context = {"Evenements": Evenement.objects.all()}
         return render(request,"stage/index.html",context)
      else:
         return redirect('connexion:login')

def show(request, id_evenement):
   if request.method == "GET":
      if request.user.is_authenticated:
         context = {"Evenement": get_object_or_404(Evenement, pk = id_evenement)}
         return render(request, "stage/show.html", context)
      else:
         return redirect('connexion:login')
