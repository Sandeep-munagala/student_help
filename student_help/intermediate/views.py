from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from login.models import IntermediateProfile

@login_required
def intermediate_home(request):
    try:
        intermediate_profile = IntermediateProfile.objects.get(user=request.user)
    except IntermediateProfile.DoesNotExist:
        pass
    if intermediate_profile:
        context = {
            'intermediate_profile': intermediate_profile,
        }
    return render(request, 'intermediate_home.html', context)

def network(request):
    return render(request, 'intermediate_network.html', {})

def computer_science(request):
    return render(request, 'computer_science.html')

def electrical_and_communications(request):
    return render(request, 'electrical_and_communications.html')

def mechanical(request):
    return render(request, 'mechanical.html')

def civil(request):
    return render(request, 'civil.html')

def chemical(request):
    return render(request, 'chemical.html')

def others(request):
    return render(request, 'others.html')