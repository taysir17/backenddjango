from django.contrib import admin
from .models import Utilisateur,Evenement,Sponsor,Partenaire,Departement,ChefDepartement
# Register your models here.

admin.site.register(Departement)
admin.site.register(Utilisateur)
admin.site.register(ChefDepartement)
admin.site.register(Sponsor)
admin.site.register(Partenaire)
@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    search_fields=['titre']