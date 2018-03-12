from django.shortcuts import render


def home(request):
    return render(request, "templates/static/home.html")
