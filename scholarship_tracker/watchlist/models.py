from django.conf import settings 
from django.db import models
from scholarships.models import Scholarship

class WatchlistEntry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name = "watchlist_entries",
    )
    scholarship= models.ForeignKey(
        Scholarship, 
        on_delete= models.CASCADE, 
        related_name = "watchlist_entries",
    )
    added_at= models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=["user","scholarship"],
                name="uniq_watchlist_user_scholarship",
            )
        ]
    def __str__(self):
        return f"{self.user} ➔ {self.scholarship}"
    