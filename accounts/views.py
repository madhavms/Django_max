# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,redirect,render
from accounts.forms import (RegistrationForm,
EditProfileForm)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash   #ENSURES THAT USER LOGGED IN AFTER PASSWORD CHANGE REDIRECT
# Create your views here.



def register(request):
	if request.method=='POST':
		form =RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account/login')
	else:
		form = RegistrationForm()
        args = {'form':form}
        return render(request,'accounts/reg_form.html',args)
@login_required
def view_profile(request):
    args={'user':request.user}
    return render(request,'accounts/profile.html',args)
@login_required
def edit_profile(request):
    if request.method=='POST':
        form =EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
        else:
            return redirect('/account/profile/edit')
    else:
        form=EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'accounts/edit_profile.html',args)
@login_required
def change_password(request):
    if request.method=='POST':
        form =PasswordChangeForm(data=request.POST,user=request.user)  #for password change user instead of instance
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user) #form.user gives user that used the form
            return redirect('/account/profile')
        else:
            return redirect('/account/change_password')
    else:
        form=PasswordChangeForm(user=request.user)    #for password change user instead of instance
        args={'form':form}
        return render(request,'accounts/change_password.html',args)
