# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from login.models import UserProfile

@login_required
def engineering_home(request):
    try:
        engineering_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        engineering_profile = None
    context = {
        'engineering_profile': engineering_profile,
    }
    return render(request, 'engineering_home.html', context)
