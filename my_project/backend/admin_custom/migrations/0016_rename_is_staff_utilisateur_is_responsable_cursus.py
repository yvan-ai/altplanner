# Generated by Django 5.1.2 on 2024-10-19 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_custom', '0015_delete_fichedesynthese'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='is_staff',
            new_name='is_responsable_cursus',
        ),
    ]
