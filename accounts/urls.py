from django.conf.urls import url
from .import views
from django.contrib.auth.views import login  #gives access to a login form
urlpatterns = [
    url(r'^$',views.home),
    url(r'^login/$',login,{'template_name':'accounts/login.html'})
]
