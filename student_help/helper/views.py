from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from login.models import UserProfile

@login_required
def log_home(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'log_home.html', context)

def network(request):
    return render(request,'network.html',{})

