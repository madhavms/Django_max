# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect



# Create your views here.

def login_redirect(request):

    return redirect('/account/login')
