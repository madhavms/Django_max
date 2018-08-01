from django.conf.urls import url, include
from django.views.generic import ListView
from blog.models import Post,Comment
from django.contrib.auth.decorators import login_required
from blog.views import HomeView,EditPost,DeletePost,DetailPost
from blog import views
urlpatterns = [

                url(r'^$',login_required(HomeView.as_view()),name='home'),
                url(r'^view',login_required(ListView.as_view(
                                    queryset=Post.objects.all().order_by("-created")[:25],
                                    template_name="blog/blog.html")),name='view'),

                url(r'^(?P<pk>\d+)$',login_required(DetailPost.as_view()),name='detail'),
                url(r'^(?P<pk>\d+)/edit$',login_required(EditPost.as_view()),name='edit'),
                url(r'^(?P<pk>\d+)/delete$',login_required(DeletePost.as_view()),name='delete'),
                url(r'^(?P<pk>\d+)/comment/$',login_required(views.add_comment_to_post),name='comment'),

]
