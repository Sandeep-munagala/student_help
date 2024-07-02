from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def log_home(request):
    return render(request, 'log_home.html', {})
