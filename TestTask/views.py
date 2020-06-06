from django.shortcuts import render, redirect

# from django.views import View
from .forms import RegisterForm


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = RegisterForm()

    return render(request, "registration/signup.html", {"form": form})
