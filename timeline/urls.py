from django.conf.urls import url
from . import views

app_name = 'timeline'

urlpatterns = [
    # url(r'$', views.home, name='home'),
    url(r'^home/', views.post_now, name='postnow'),
]
