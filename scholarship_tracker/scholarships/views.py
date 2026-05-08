from datetime import date
from django.shortcuts import render
from watchlist.models import WatchlistEntry
from .models import Scholarship

def scholarship_list(request):
    qs=Scholarship.objects.filter(is_active=True)
    q=request.GET.get("q")
    country= request.GET.get("country")
    if q:
        qs=qs.filter(name__icontains=q)
    if country:
        qs=qs.filter(country__iexact=country)
    today = date.today()
    items=[]
    for s in qs:
        days_left= (s.deadline-today).days
        if days_left <=7:
            badge_color="red"
        elif days_left<=30:
            badge_color="orange"
        else:
            badge_color="green"
        items.append({
            "obj":s,
            "days_left":days_left,
            "badge_color":badge_color,
        })
    countries = Scholarship.objects.values_list("country", flat=True).distinct()
    saved_ids = []
    if request.user.is_authenticated:
        saved_ids = list(
            WatchlistEntry.objects.filter(user=request.user).values_list(
                "scholarship_id", flat=True
            )
        )
    return render(
        request,
        "scholarships/list.html",
        {
            "items": items,
            "q": q or "",
            "selected_country": country or "",
            "countries": countries,
            "saved_ids": saved_ids,
        },
    )