from django.conf.urls import url
from home.views import HomeView
from django.contrib.auth.decorators import login_required
urlpatterns=[
    url(r'^$',login_required(HomeView.as_view()),name='home')


]
