# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from home.forms import HomeForm
from django.shortcuts import render
class HomeView(TemplateView):
    template_name='home/home.html'

    def get(self,request):
        form=HomeForm()
        return render(request,)
