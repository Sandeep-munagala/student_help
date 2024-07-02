from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import SignUpForm
from .models import UserProfile

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
            messages.success(request, "You have been logged in.")
            return redirect('log_home')
        else:
            messages.error(request, "Invalid username/password.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user=user,
                dob=form.cleaned_data['dob'],
                college=form.cleaned_data['college'],
                year=form.cleaned_data['year'],
                branch=form.cleaned_data['branch'],
            )
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect('home')
        else:
            # Handle form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            return redirect('register')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
