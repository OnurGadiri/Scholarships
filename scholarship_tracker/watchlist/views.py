from datetime import date 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect 
from django.views.decorators.http import require_POST
from scholarships.models import Scholarship
from .models import WatchlistEntry

def _badge_for_scholarship(s):
    today = date.today()
    days_left = (s.deadline - today).days
    if days_left <= 7:
        badge_color = "red"
    elif days_left <= 30:
        badge_color = "orange"
    else:
        badge_color = "green"
    return days_left, badge_color

@login_required
def watchlist_list(request):
    entries= (
        WatchlistEntry.objects.filter(user=request.user).select_related("scholarship").order_by("scholarship__deadline")
    ) 
    items= []
    for entry in entries:
        s= entry.scholarship
        days_left, badge_color = _badge_for_scholarship(s)
        items.append({"obj":s,"days_left":days_left,"badge_color":badge_color})
    return render(request, "watchlist/list.html",{"items":items})   
@login_required
@require_POST
def watchlist_add(request):
    scholarship_id = request.POST.get("scholarship_id")
    scholarship=get_object_or_404(
        Scholarship , pk=scholarship_id , is_active=True
    )
    WatchlistEntry.objects.get_or_create(
        user= request.user , 
        scholarship = scholarship,
    )
    return redirect("/")
@login_required
@require_POST
def watchlist_remove(request):
    scholarship_id = request.POST.get("scholarship_id")
    scholarship=get_object_or_404(Scholarship , pk=scholarship_id, is_active=True)
    WatchlistEntry.objects.filter(
        user= request.user, 
        scholarship_id=scholarship_id,
    ).delete()
    return redirect("/")