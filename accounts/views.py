from django.shortcuts import render, redirect

from .forms import UserProfileForm, MissionForm
from .models import User, UserProfile, Mission

# Create your views here.
def home(request):
    return render(request, 'home.html')

# PROFILE SECTION
def profiles(request):
    users = User.objects.all()
    context = {'users' : users,}
    return render(request, "profiles.html", context)

def profile_edit(request, user_id):
    if request.method == "GET":
        profile = UserProfile.objects.filter(user_id = user_id).first()
        form = UserProfileForm(instance=profile)
        context = {'form': form}
        return render(request, 'profile_edit.html', context)
    
    if request.method == "POST":
        profile = UserProfile.objects.filter(user_id = user_id).first()
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profiles")
        else:
            context = {'form', form}
            return render(request, "profile_edit.html", context)
    
    context = {"form" : UserProfileForm}
    return render(request, 'profile_edit.html', context)
        

#MISSIONS SECTION
def missions(request):
    all_missions = Mission.objects.all()
    context = {'missions' : all_missions ,}
    return render(request, 'missions.html', context)

def mission_add(request):
    if request.method == "GET":
        form = MissionForm()
        context = {'form' : form}
        return render(request, 'mission_add.html', context)
    
    if request.method == "POST":
            form = MissionForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect ('missions')
    
    context = {'form': MissionForm}
    return render(request, 'mission_add.html', context)
    
    

def mission_edit(request, mission_id):
    if request.method == "GET":
        mission = Mission.objects.filter(pk = mission_id).first()
        form = MissionForm(instance=mission)
        context = {'form': form}
        return render(request, 'mission_edit.html', context)
    
    if request.method == "POST":
        mission = Mission.objects.filter(pk = mission_id).first()
        form = MissionForm(request.POST, request.FILES, instance=mission)
        if form.is_valid():
            form.save()
            return redirect ('missions')

        context = {'form': MissionForm}
        return render(request, 'mission_edit.html', context)
    
def mission_delete(request, mission_id):
    mission = Mission.objects.filter(pk = mission_id).first()
    mission.delete()
    return redirect('missions')