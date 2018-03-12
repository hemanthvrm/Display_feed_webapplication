from django.conf.urls import url
from .views import login, signup

app_name = 'accounts'

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^signup/', signup, name='signup'),

]
