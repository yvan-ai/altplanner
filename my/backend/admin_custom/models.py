# admin_custom/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Utilisateur(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        (1, 'Admin'),
        (2, 'Apprenti'),
        (3, 'Tuteur pédagogique'),
        (4, 'Enseignant'),
        (5, 'Maitre d apprentissage'),
        (6, 'coordinatrice d apprentissage'),
        # Ajoute d'autres types d'utilisateurs ici
    )

    email = models.EmailField(unique=True)
    #username = models.CharField(max_length=150, unique=True, default='')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    #date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    objects = UserManager()

    #USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','first_name', 'last_name', 'user_type']  

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change le related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change le related_name
        blank=True
    )

    def __str__(self):
        return self.email
    
class Entreprise(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

class Formation(models.Model):
    intitule = models.CharField(max_length=255, primary_key=True)

class Groupe(models.Model):
    numero = models.AutoField(primary_key=True)
    capacite = models.IntegerField()
    formation = models.ForeignKey(Formation, on_delete=models.SET_NULL,blank=True,null=True)

class JournalDeFormation(models.Model):
    numero = models.AutoField(primary_key=True)
    date_derniere_modification = models.DateField()

class RapportFinal(models.Model):
    numero = models.OneToOneField(JournalDeFormation, primary_key=True, on_delete=models.CASCADE)
    date_publication = models.DateField()

class RapportPING(models.Model):
    numero = models.OneToOneField(JournalDeFormation, primary_key=True, on_delete=models.CASCADE)
    date_publication = models.DateField()

class Presentation(models.Model):
    numero = models.OneToOneField(JournalDeFormation, primary_key=True, on_delete=models.CASCADE)
    date_publication = models.DateField()

class MaitreApprentissage(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    mail = models.EmailField()
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=20,blank=True)
    prenom = models.CharField(max_length=255)
    mdp = models.CharField(max_length=255)
    entreprise = models.ForeignKey(Entreprise,blank=True, on_delete=models.SET_NULL, null=True)

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    mail = models.EmailField()
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=20)
    prenom = models.CharField(max_length=255)
    mdp = models.CharField(max_length=255)

class TuteurPedagogique(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    mail = models.EmailField()
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=20, blank=True)
    prenom = models.CharField(max_length=255)
    mdp = models.CharField(max_length=255)

class CoordinatriceApprentissage(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    mail = models.EmailField()
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=20,blank=True)
    prenom = models.CharField(max_length=255)
    mdp = models.CharField(max_length=255)

class Apprenti(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    mail = models.EmailField()
    date_naissance = models.DateField(null=True)
    telephone = models.CharField(max_length=20,blank=True)
    prenom = models.CharField(max_length=255)
    mdp = models.CharField(max_length=255)
    tuteur_pedagogique = models.ForeignKey(TuteurPedagogique,blank=True,null=True, on_delete=models.SET_NULL)
    numero_journal = models.ForeignKey(JournalDeFormation,blank=True,null=True, on_delete=models.SET_NULL)
    groupe = models.ForeignKey(Groupe,blank=True,null=True, on_delete=models.SET_NULL)
    maitre_apprentissage = models.ForeignKey(MaitreApprentissage,blank=True,null=True, on_delete=models.SET_NULL)
    coordinatrice_apprentissage = models.ForeignKey(CoordinatriceApprentissage,blank=True,null=True, on_delete=models.SET_NULL)


class Enseignant(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    mail = models.EmailField()
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=20,blank=True)
    prenom = models.CharField(max_length=255)
    mdp = models.CharField(max_length=255)

class EntretienSemestriel(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    semestre = models.IntegerField()
    note = models.FloatField()
    commentaire = models.TextField()
    maitre_apprentissage = models.ForeignKey(MaitreApprentissage, on_delete=models.CASCADE)
    tuteur_pedagogique = models.ForeignKey(TuteurPedagogique, on_delete=models.CASCADE)
    apprenti = models.ForeignKey(Apprenti, on_delete=models.CASCADE)

class Soutenance(models.Model):
    id = models.AutoField(primary_key=True)
    evaluation = models.ForeignKey('Evaluation', on_delete=models.CASCADE)
    semestre = models.IntegerField()
    note = models.FloatField()
    commentaire = models.TextField()

# Jury
class Jury(models.Model):
    id = models.AutoField(primary_key=True)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)

# Formulaire
class Formulaire(models.Model):
    note = models.FloatField()
    entretien = models.ForeignKey(EntretienSemestriel, on_delete=models.CASCADE)

# Echeance
class Echeance(models.Model):
    id = models.AutoField(primary_key=True)
    date_debut = models.DateField()
    date_fin = models.DateField()

# Evaluation
class Evaluation(models.Model):
    id = models.AutoField(primary_key=True)
    note = models.FloatField()
    commentaire = models.TextField()
    echeance = models.ForeignKey(Echeance, on_delete=models.CASCADE)
    apprenti = models.ForeignKey(Apprenti, on_delete=models.CASCADE)

# Semestre
class Semestre(models.Model):
    id = models.AutoField(primary_key=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    echeance = models.ForeignKey(Echeance, on_delete=models.CASCADE)

# Fiche de Synthèse
class FicheDeSynthese(models.Model):
    numero = models.OneToOneField(JournalDeFormation, primary_key=True, on_delete=models.CASCADE)
    date_publication = models.DateField()

# Membre Jury
class MembreJury(models.Model):
    membre1 = models.ForeignKey(Jury, related_name='membre1', on_delete=models.CASCADE)
    membre2 = models.ForeignKey(Jury, related_name='membre2', on_delete=models.CASCADE)
    jury = models.ForeignKey(Jury, related_name='jury', on_delete=models.CASCADE)

