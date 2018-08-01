# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=50)
    post = models.TextField()
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True) #add date when object was created
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view', kwargs={'pk': self.pk})
class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
