# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=500, default='DEFAULT VALUE')
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True) #add date when object was created

    def __str__(self):
        return self.post
