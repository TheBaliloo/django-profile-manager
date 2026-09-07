from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class User(AbstractUser):
    pass

    def __str__(self):
        return self.email
    
    
class UserProfile(models.Model):
    G = "---"
    H = "Homme"
    F = "Femme"
    GENDER = {
        G : "---",
        H : "Homme",
        F : "Femme",
    }
        
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    
    # Fields goes here...
    #....................
    
    display_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=5, choices=GENDER, default=GENDER["---"])
    
    # Fields ends here...
    
    def __str__(self):
        return f"Profile for {self.user.email}"
    
    class Meta: 
        verbose_name = 'User Profile'
        verbose_name_plural = "User Profiles"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)
        
class Mission(models.Model):
    #MISSION TYPES CHOICES
    NN = "---"
    BR = "Brouillage"
    CC = "Controle de conformite"
    PH = "Controle Points Hauts"
    EMF = "Mesure EMF"
    
    MISSION_TYPE = {
        NN : "---",
        BR : "Brouillage",
        CC : "Controle de conformite",
        PH : "Controle Points Hauts",
        EMF : "Mesure EMF",
    }
    
    #ETAT CHOICES
    NN = "---"
    WAITING = "En attente"
    RUNNING = "En cours"
    DONE = "Teminee"
    
    ETAT = {
        NN : "---",
        WAITING : "En attente",
        RUNNING : "En cours",
        DONE : "Terminee",
    }
    
    numero = models.CharField(max_length=5, blank=False, null=False)
    date_heure = models.DateTimeField(auto_now=False, blank=True, null=True)
    type = models.CharField(max_length=25, choices=MISSION_TYPE, default=MISSION_TYPE["---"])
    region = models.CharField(max_length=50, null=True, blank=True)
    etat =  models.CharField(max_length=25, choices=ETAT, default=ETAT["---"])
    responsable = models.CharField(max_length=50, null=True, blank=True)