from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import (login,logout,password_reset,
password_reset_done,password_reset_confirm,password_reset_complete )#gives access to a login form

urlpatterns = [


    url(r'^login/$',login,{'template_name':'accounts/login.html'},name='login'),
    url(r'^logout/$',logout,{'template_name':'accounts/logout.html'},name='logout'),
    url(r'^register/$',views.register,name="register"),
    url(r'^profile/$',views.view_profile,name="view_profile"),
    url(r'^profile/edit/$',views.edit_profile,name="edit_profile"),
    url(r'^change_password/$',views.change_password,name="change_password"),
    url(r'^reset_password/$',password_reset,{'template_name':'accounts/password_reset.html'},name="reset_password"),
    url(r'^reset_password_done/$',password_reset_done,name="password_reset_done"),  #####USE THE DEFAULT NAME 'password_reset_done' else error shows up
                                                                                   ##ERROR MESSAGE:Reverse for 'password_reset_done' not found. 'password_reset_done'
                                                                                   #is not a valid view function or pattern name.
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    password_reset_confirm,name='password_reset_confirm'),                       ###CONNECTION REFUSED ERROR:https://stackoverflow.com/questions/5802189/django-errno-111-connection-refused#5802348
    url(r'^reset_password_complete/$',password_reset_complete,{'template_name':'accounts/password_reset_complete.html'},name="password_reset_complete"),
]
 
