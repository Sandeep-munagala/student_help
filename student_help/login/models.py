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