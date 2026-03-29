from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm, UserProfileForm


def register(request):
    if request.user.is_authenticated:
        return redirect("scholarship_list")
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("scholarship_list")
    else:
        form = StudentRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile_edit")
    else:
        form = UserProfileForm(instance=profile)
    return render(request, "accounts/profile.html", {"form": form})
