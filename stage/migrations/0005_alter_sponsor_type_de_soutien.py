# Generated by Django 5.0.1 on 2024-01-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0004_alter_evenement_lieu_alter_evenement_titre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='type_de_soutien',
            field=models.CharField(max_length=20),
        ),
    ]
