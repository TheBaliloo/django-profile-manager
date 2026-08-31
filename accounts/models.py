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
    user = models.OneToOneField(
        'accounts.User', 
        on_delete=models.CASCADE,
    )
    
    # Fields goes here...
    #....................
    
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