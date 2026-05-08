from django.urls import path
from . import views
urlpatterns = [
    path("", views.watchlist_list, name="watchlist_list"),
    path("add/", views.watchlist_add, name="watchlist_add"),
    path("remove/", views.watchlist_remove, name="watchlist_remove"),
]