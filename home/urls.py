from django.conf.urls import url
from home.views import HomeView,PostView,EditPost
from django.contrib.auth.decorators import login_required
urlpatterns=[
    url(r'^$',login_required(HomeView.as_view()),name='home'),
    url(r'^posts/',login_required(PostView.as_view()),name='posts'),
    url('post/<int:pk>/edit/',login_required(EditPost.as_view()), name='post_edit'),
]
