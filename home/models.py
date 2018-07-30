# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=50, default='DEFAULT VALUE')
    post = models.CharField(max_length=500, default='DEFAULT VALUE')
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True) #add date when object was created
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
