from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm , UserChangeForm as BaseUserChangeForm
from django import forms

from .models import User, UserProfile

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
        
class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")
        

# Profile forms
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"