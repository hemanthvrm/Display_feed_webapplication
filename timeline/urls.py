from django.conf.urls import url
from . import views

app_name = 'timeline'

urlpatterns = [
    url(r'$', views.home, name='home'),
    url(r'^post/', views.post_now, name='postnow'),
]
