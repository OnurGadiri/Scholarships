from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name= "profile", 
    )
    field_of_study=models.CharField(max_length=150, blank=True)
    target_country=models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.user.get_username()