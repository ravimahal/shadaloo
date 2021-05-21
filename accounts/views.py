from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Profile
from . import forms

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        # request.POST returns a dictionary of names and values
        # usercreationform returns a instance/object
        form = UserCreationForm(request.POST)
        form.is_valid() #boolean True/False
        if form.is_valid():
            user = form.save()
            #create user settings entry too
            profile = Profile()
            #requires an instance/object to be assigned to 'user' as its a one-to-one field with User model
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')
    elif request.method == 'GET':
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form' : form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home')
    elif request.method == 'GET':
        form = AuthenticationForm(request.POST)
    
    return render(request, 'login.html', {'form' : form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')

@login_required(login_url="/accounts/login")
def profile_view(request):
    if request.method == 'POST':

        #get the user from db
        db_user_instance = User.objects.get(username = request.user.username)
        db_profile_instance =  Profile.objects.get(user = db_user_instance)

        # bind the forms with new data from POST, select to update existing instance
        user_form = forms.UserProfile(request.POST, instance = db_user_instance)
        extended_form = forms.ExtendedProfile(request.POST, instance = db_profile_instance)

        if user_form.is_valid() and extended_form.is_valid():
            user_form.save()
            #save the related 1 to many model (profile)
            ext_profile_instance = extended_form.save(commit=False) #create the instance, dont commit to database
            #add user object to profile instance to allow us to save
            ext_profile_instance.user = request.user
            ext_profile_instance.save()

    elif request.method == 'GET':
        #first visit to profile page
        db_user = User.objects.get(username = request.user.username)
        db_profile = Profile.objects.get(user = db_user)
        user_form = forms.UserProfile(instance = db_user)    
        extended_form = forms.ExtendedProfile(instance = db_profile)
    return render(request, 'profile.html', {'user_form': user_form, 'extended_form': extended_form})