from django.shortcuts import render
from Home.forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, "index.html")


def patient_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("user_dashboard")
        else:
            return redirect("login_page")
    context = {}
    return render(request, 'patient-login.html', context)


def logout_page(request):
    logout(request)
    return redirect("index")


def patient_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            form.save()
            new_user = authenticate(username=username, password=password)
            new_user.save()
            if new_user is not None:
                login(request, new_user)
                return redirect("user_dashboard")
    else:
        form = SignupForm()
    context = {"form": form}
    return render(request, 'patient-signup.html', context)


def doctor_login(request):
    return render(request, 'doc-login.html')


def doctor_dashboard(request):
    return render(request, 'doc-login.html')
