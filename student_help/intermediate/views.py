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
