# Generated by Django 5.0.1 on 2024-01-31 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0005_alter_sponsor_type_de_soutien'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='photo',
            field=models.CharField(default=None, max_length=5000, null=True),
        ),
    ]