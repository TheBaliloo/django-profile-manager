from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserProfileForm
from .models import User, UserProfile

# Create your views here.
def home(request):
    users = User.objects.all()
    context = {'users' : users,}
    return render(request, 'home.html', context)


def edit(request, user_id):
    if request.method == "GET":
        profile, created = UserProfile.objects.get_or_create(user_id = user_id)
        form = UserProfileForm(request.GET, request.FILES, instance=profile)
        context = {'form': form}
        return render(request, 'edit.html', context)
        
    if request.method == "POST":
            profile, created = UserProfile.objects.get_or_create(user_id = user_id)
            form = UserProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
            context = {'form': form}
            return render(request, 'edit.html', context)

    context = {'form': UserProfileForm}
    return render(request, 'edit.html', context)

