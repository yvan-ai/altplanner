# Generated by Django 5.1.2 on 2024-10-19 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_custom', '0013_alter_apprenti_date_naissance'),
    ]

    operations = [
        migrations.CreateModel(
            name='FicheSynthese',
            fields=[
                ('numero', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='admin_custom.journaldeformation')),
                ('document', models.FileField(blank=True, null=True, upload_to='ficheSyn_doc/')),
                ('date_publication', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='presentation',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='presentation_doc/'),
        ),
        migrations.AddField(
            model_name='rapportfinal',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='rapportFinal_doc/'),
        ),
        migrations.AddField(
            model_name='rapportping',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='ping_doc/'),
        ),
    ]