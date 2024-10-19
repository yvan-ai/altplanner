# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Utilisateur, MaitreApprentissage, Apprenti, TuteurPedagogique, CoordinatriceApprentissage, Enseignant
from django.contrib.auth.hashers import make_password


@receiver(post_save, sender=Utilisateur)
def create_specific_user(sender, instance, created, **kwargs):
    if created:
        password_hashed = make_password(instance.password)
        if instance.user_type == 5:  # Maitre d'apprentissage
            MaitreApprentissage.objects.create(
                nom=instance.last_name,
                prenom=instance.first_name,
                mail=instance.email,
                mdp=instance.password  # Assure-toi que le mot de passe est haché
                # L'entreprise est à gérer séparément ou par défaut
            )
        elif instance.user_type == 2:  # Apprenti
            Apprenti.objects.create(
                nom=instance.last_name,
                prenom=instance.first_name,
                mail=instance.email,
                mdp=password_hashed
                # Tu peux ajouter les relations ici comme tuteur_pedagogique, groupe, etc.
            )
        elif instance.user_type == 3:  # Tuteur pédagogique
            TuteurPedagogique.objects.create(
                nom=instance.last_name,
                prenom=instance.first_name,
                mail=instance.email,
                mdp=password_hashed
            )
        elif instance.user_type == 6:  # Coordinatrice d'apprentissage
            CoordinatriceApprentissage.objects.create(
                nom=instance.last_name,
                prenom=instance.first_name,
                mail=instance.email,
                mdp=password_hashed
            )
        elif instance.user_type == 4:  # Enseignant
            Enseignant.objects.create(
                nom=instance.last_name,
                prenom=instance.first_name,
                mail=instance.email,
                mdp=password_hashed
            )
