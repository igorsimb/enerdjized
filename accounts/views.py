from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import ProfileForm
from .models import User


def profile_view(request, username=None):
    """
    Displays the profile of the user with the given username using @username syntax.
    If no username is provided, the profile of the currently logged in user is displayed.
    """
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect("account_login")
    return render(request, "account/profile.html", {"profile": profile})


@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")

    if request.path == reverse("profile_onboarding"):
        onboarding = True
    else:
        onboarding = False

    context = {"form": form, "onboarding": onboarding}
    return render(request, "account/profile_edit.html", context)
