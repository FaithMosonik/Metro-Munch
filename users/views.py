from django.shortcuts import render, redirect
from django.contrib.auth import login
from . import forms


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("core:home")
    else:
        form = forms.CustomUserCreationForm()

    return render(request, "registration/signup.html", {"form": form})
