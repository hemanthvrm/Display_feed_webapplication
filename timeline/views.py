from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
import requests


def home(request):
    tweet = Post.objects.all()
    print(tweet)
    context = {
        'tweets': tweet
    }
    return render(request, "timeline/home.html", context)


@login_required
def post(request):
    if request.method == "POST":
        check_cached = ('user_info' in request.session)

        if not check_cached:
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
            resp = requests.get('http://freegeoip.net/json/%s' % ip_address)
            request.session['user_info'] = resp.json()

        user_info = request.session['user_info']

        if request.POST["listeningpost"]:
            print("i am here")
            post = Post()
            post.author = request.user
            post.songname = request.POST["listeningpost"]
            post.created_date = timezone.datetime.now()
            post.author_ipaddress = user_info['ip']
            post.author_city = user_info['country_name']
            print("i am here")
            post.save()

    # else:
    #     return render(request, "timeline/home.html")
