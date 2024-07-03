from django.contrib import admin
from .models import UserProfile,IntermediateProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(IntermediateProfile)