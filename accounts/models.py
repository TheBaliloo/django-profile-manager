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