# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,redirect,render
from accounts.forms import RegistrationForm,EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):

    return render(request,'accounts/home.html')

def register(request):
	if request.method=='POST':
		form =RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = RegistrationForm()
        args = {'form':form}
        return render(request,'accounts/reg_form.html',args)

def view_profile(request):
    args={'user':request.user}
    return render(request,'accounts/profile.html',args)

def edit_profile(request):
    if request.method=='POST':
        form =EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/')
        else:
            return redirect('/account/edit')
    else:
        form=EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'accounts/edit_profile.html',args)
