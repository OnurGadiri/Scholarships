from django.db import models

class Scholarship(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=150)
    language_requirement = models.CharField(max_length=100)
    funding_amount = models.CharField(max_length=100)
    deadline = models.DateField()
    application_link = models.URLField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.country})"