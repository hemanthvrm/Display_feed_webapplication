from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def login(request):
    url = "accounts/login.html"
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["psw"])
        if user is not None:
            url = "timeline/home.html"
            login(request, user)
            return render(request, url)
        else:
            context = {
                "error": "Username and password was incorrect"
            }
            return render(request, url, context)
    else:
        return render(request, url)


def signup(request):
    url = "accounts/signup.html"
    if request.method == "POST":
        if request.POST["psw"] == request.POST["psw1"]:
            url = "accounts/login.html"
            user = User.objects.create_user(request.POST["username"], , request.POST["psw"])
            user.save()
            return render(request, url)

        else:
            context = {
                "error": "Password doesn't match. Please try again"
            }
            return render(request, url, context)

    else:
        return render(request, url)
