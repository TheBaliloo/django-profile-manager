from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile


from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name = 'User profile'
    verbose_name_plural = 'User Profiles'

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    add_fieldsets = (
        ( None, {
            "classes": ("wide",),
            "fields": ("username","email", "password1", "password2"),
            },
        ),
    )
    list_display = [
        'email', 
        'username',
    ]
    inlines = [UserProfileInline]
    
    def get_inline_instances(self, request, obj = None):
        if obj is None:
            return []
        return super().get_inline_instances(request, obj)
        
    


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)