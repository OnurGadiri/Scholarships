from django.contrib import admin
from .models import WatchlistEntry


@admin.register(WatchlistEntry)
class WatchlistEntryAdmin(admin.ModelAdmin):
    list_display = ("user", "scholarship", "added_at")
    list_filter = ("added_at",)
    search_fields = ("user__username", "scholarship__name", "scholarship__country")