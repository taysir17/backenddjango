from django.db import models
from django.contrib.auth.models import User
import uuid 

class Departement(models.Model):
    id_dep = models.CharField(primary_key=True, max_length=10)  
    nom = models.CharField(max_length=50)
    etage = models.IntegerField()
    nb_utilisateurs = models.IntegerField()
    chef_departement = models.OneToOneField('Utilisateur', related_name='department_relation', on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Utilisateur(models.Model):
    id_utilisateur = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField(max_length=20, unique=True, default=None, null=True,)
    nom = models.CharField(max_length=20, unique=True)
    prenom = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    numero_telephone = models.CharField(max_length=15)
    age = models.IntegerField()
    diplome = models.CharField(max_length=50)
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    departement = models.ForeignKey('Departement', default=None, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom} {self.prenom}"

class ChefDepartement(Utilisateur):
    niveau_professionnel = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Sponsor(models.Model):
    id_sponsor = models.CharField(primary_key=True, max_length=10)
    nom = models.CharField(max_length=20, unique=True)
    type_de_soutien = models.CharField(max_length=20)
    def __str__(self):
        return self.nom

class Partenaire(models.Model):
    id_partenaire = models.CharField(primary_key=True, max_length=10)
    nom = models.CharField(max_length=20, unique=True)
    adresse = models.CharField(max_length=20, unique=True)
    statut = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.nom
        
class Evenement(models.Model):
    id_evenement = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    titre = models.CharField(max_length=100)
    photo  = models.CharField(max_length=5000, default=None, null=True,)
    date = models.DateField()
    lieu = models.CharField(max_length=20)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    nb_participant = models.IntegerField()
    chef = models.ForeignKey(Utilisateur, related_name='organised_events', on_delete=models.CASCADE)
    sponsors = models.ManyToManyField(Sponsor)
    partenaires = models.ManyToManyField(Partenaire)
    participants = models.ManyToManyField(Utilisateur)
    def __str__(self):
        return self.titre