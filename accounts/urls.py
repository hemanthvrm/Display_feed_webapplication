from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/', views.loginpage, name='login'),
    url(r'^signup/', views.signuppage, name='signup'),

]
