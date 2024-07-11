from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    college = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=100, blank=True)
    minor = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class IntermediateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    college = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    
class College(models.Model):
    college = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.college
    
class Connection(models.Model):
    intermediate_profile = models.ForeignKey(IntermediateProfile, on_delete=models.CASCADE, related_name='connections_as_intermediate')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='connections_as_user')
    is_connected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Connection from {self.intermediate_profile.user.username} to {self.user_profile.user.username} - {'Connected' if self.is_connected else 'Pending'}"