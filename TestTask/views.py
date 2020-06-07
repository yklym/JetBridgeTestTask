from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from .forms import RegisterForm
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


@login_required
def users_list(request):
    users = ViralUser.objects.order_by("id")
    return render(request, 'ViralUser/usersList.html', {"profiles": users})


@login_required
def user_page(request, pk):
    error_not_found = False
    profile = None
    try:
        profile = ViralUser.objects.get(id=pk)
    except ObjectDoesNotExist:
        error_not_found = True
    return render(request, 'ViralUser/userPage.html', {"error404": error_not_found, "profile": profile})
