from django.conf.urls import url, include
from django.views.generic import ListView,DetailView
from blog.models import Post
from django.contrib.auth.decorators import login_required
from blog.views import HomeView,EditPost
urlpatterns = [

                url(r'^$',login_required(HomeView.as_view()),name='home'),
                url(r'^view',login_required(ListView.as_view(
                                    queryset=Post.objects.all().order_by("-created")[:25],
                                    template_name="blog/blog.html")),name='view'),

                url(r'^(?P<pk>\d+)$',login_required(DetailView.as_view(model=Post,template_name='blog/post.html'))),
                url(r'^(?P<pk>\d+)/edit$',login_required(EditPost.as_view()),name='edit')

            ]
