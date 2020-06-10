from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from .forms import RegisterForm, UpdateForm
from .models import ViralUser


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("/users")
    else:
        form = RegisterForm()

    return render(request, "registration/signup.html", {"form": form})


@login_required(redirect_field_name="/login")
def users_list(request):
    users = ViralUser.objects.order_by("id")
    return render(request, 'ViralUser/usersList.html', {"profiles": users})


@login_required(redirect_field_name="/login")
def user_page(request, pk):
    error_not_found = False
    profile = None
    try:
        profile = ViralUser.objects.get(id=pk)
    except ObjectDoesNotExist:
        error_not_found = True
    is_owner = request.user.profile.id == profile.id
    return render(request, 'ViralUser/userPage.html', {"error404": error_not_found, "profile": profile, "is_owner": is_owner})


def user_update_page(request, pk):
    try:
        profile = ViralUser.objects.get(id=pk)
    except ObjectDoesNotExist:
        return render(request, "ViralUser/updateUser.html",
                      {"error404": True})

    is_owner = request.user.profile.id == profile.id
    if not is_owner:
        return render(request, "ViralUser/updateUser.html",
                      {"error403": True})

    if request.method == "POST":
        form = UpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(f"/users/{profile.id}")
    else:
        form = UpdateForm()

    return render(request, "ViralUser/updateUser.html", {"form": form})

