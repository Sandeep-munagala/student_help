from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{})

def help(request):
    return render(request, 'help.html',{})

def resources(request):
    return render(request, 'resources.html',{})

def about(request):
    return render(request, 'about.html',{})

def contact(request):
    return render(request, 'contact.html',{})

def login_view(request):
    return render(request, 'login.html',{})

def register(request):
    return render(request, 'register.html',{})

# Create your views here.
