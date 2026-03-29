from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "field_of_study", "target_country")
    search_fields = ("user__username", "field_of_study", "target_country")
