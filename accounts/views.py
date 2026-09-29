from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import StudentProfile, College
from .forms import RegisterForm, ProfileForm


def register_view(request):

    form = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data["password"]
            )

            user.save()

            StudentProfile.objects.create(
                user=user,
                college=College.objects.first(),
                department="",
                semester=1,
                roll_number="",
                phone=""
            )

            return redirect("login")

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect("/")

    return render(
        request,
        "accounts/login.html"
    )


def logout_view(request):

    logout(request)

    return redirect("/")
from django.contrib.auth.decorators import login_required


@login_required
def profile_view(request):

    profile = StudentProfile.objects.get(
        user=request.user
    )

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect("profile")

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        "accounts/profile.html",
        {
            "form": form,
            "profile": profile
        }
    )