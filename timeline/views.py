from django.shortcuts import render


def home(request):
    return render(request, "timeline/home.html")


def post(request):
    return render(request, "timeline/home.html")
#     if request.method == "POST":
