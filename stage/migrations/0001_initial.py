# Generated by Django 5.0.1 on 2024-01-30 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id_utilisateur', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20, unique=True)),
                ('prenom', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('numero_telephone', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('diplome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id_dep', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('etage', models.IntegerField()),
                ('nb_utilisateurs', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id_partenaire', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20, unique=True)),
                ('adresse', models.CharField(max_length=20, unique=True)),
                ('statut', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id_sponsor', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20, unique=True)),
                ('type_de_soutien', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChefDepartement',
            fields=[
                ('utilisateur_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stage.utilisateur')),
                ('niveau_professionnel', models.CharField(max_length=20, unique=True)),
            ],
            bases=('stage.utilisateur',),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='departement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage.departement'),
        ),
        migrations.AddField(
            model_name='departement',
            name='chef_departement',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='department_relation', to='stage.utilisateur'),
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id_evenement', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=20, unique=True)),
                ('date', models.DateField()),
                ('lieu', models.CharField(max_length=20, unique=True)),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('nb_participant', models.IntegerField()),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organised_events', to='stage.utilisateur')),
                ('participants', models.ManyToManyField(to='stage.utilisateur')),
                ('partenaires', models.ManyToManyField(to='stage.partenaire')),
                ('sponsors', models.ManyToManyField(to='stage.sponsor')),
            ],
        ),
    ]
