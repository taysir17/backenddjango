# Generated by Django 5.0.1 on 2024-02-02 08:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0009_utilisateur_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='id_evenement',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
