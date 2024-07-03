from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login.models import UserProfile, IntermediateProfile

@login_required
def log_home(request):
    user_profile = None
    intermediate_profile = None

    # Check if UserProfile exists
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        pass

    # Check if IntermediateProfile exists
    try:
        intermediate_profile = IntermediateProfile.objects.get(user=request.user)
    except IntermediateProfile.DoesNotExist:
        pass

    # If user_profile exists and is intermediate, update fields from intermediate_profile
    if user_profile:
        context = {
            'user_profile': user_profile,
        }
    if intermediate_profile:
        context = {
            'intermediate_profile': intermediate_profile,
        }
    return render(request, 'log_home.html', context)

def network(request):
    return render(request, 'network.html', {})
