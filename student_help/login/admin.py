from django.contrib import admin
from .models import UserProfile,IntermediateProfile,College,Connection
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(IntermediateProfile)
admin.site.register(College)
admin.site.register(Connection)