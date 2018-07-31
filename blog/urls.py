from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.contrib.auth.decorators import login_required
from blog.views import HomeView
urlpatterns = [

                url(r'^$',login_required(HomeView.as_view()),name='home'),
                url(r'^view',login_required(ListView.as_view(
                                    queryset=Post.objects.all().order_by("-created")[:25],
                                    template_name="blog/blog.html")),name='view'),
            ]
