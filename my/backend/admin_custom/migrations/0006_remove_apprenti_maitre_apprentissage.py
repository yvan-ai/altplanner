# Generated by Django 5.1.2 on 2024-10-17 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_custom', '0005_alter_apprenti_maitre_apprentissage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apprenti',
            name='maitre_apprentissage',
        ),
    ]