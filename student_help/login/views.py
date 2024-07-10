from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import EngineeringSignUpForm, IntermediateSignUpForm
from .models import UserProfile, IntermediateProfile

def home(request):
    return render(request, 'home.html', {})

def help(request):
    return render(request, 'help.html', {})

def resources(request):
    return render(request, 'resources.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Check the type of profile and redirect accordingly
            try:
                user_profile = UserProfile.objects.get(user=user)
                return redirect('engineering_home')
            except UserProfile.DoesNotExist:
                try:
                    intermediate_profile = IntermediateProfile.objects.get(user=user)
                    return redirect('intermediate_home')
                except IntermediateProfile.DoesNotExist:
                    messages.error(request, "Profile does not exist.")
                    return redirect('login')
        else:
            messages.error(request, "Invalid username/password.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_engineering(request):
    if request.method == 'POST':
        form = EngineeringSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user=user,
                dob=form.cleaned_data.get('dob'),
                college=form.cleaned_data.get('college'),
                year=form.cleaned_data.get('year'),
                department=form.cleaned_data.get('department'),
                minor=form.cleaned_data.get('minor'),
            )
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            return redirect('register_engineering')  # Redirect to registration page or handle as per your URL setup
    else:
        form = EngineeringSignUpForm()
    return render(request, 'register.html', {'form': form, 'form_type': 'engineering'})

def register_intermediate(request):
    if request.method == 'POST':
        form = IntermediateSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            IntermediateProfile.objects.create(
                user=user,
                dob=form.cleaned_data.get('dob'),
                college=form.cleaned_data.get('college'),
            )
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            return redirect('register_intermediate')  # Redirect to registration page or handle as per your URL setup
    else:
        form = IntermediateSignUpForm()
    return render(request, 'register.html', {'form': form, 'form_type': 'intermediate'})


