# Generated by Django 5.1.2 on 2024-10-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_custom', '0009_remove_apprenti_groupe'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='tuteur_pedagogique',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
