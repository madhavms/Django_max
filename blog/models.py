# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    tilte=models.CharField(max_length=140)
    body=models.TextField()
    date=models.DateTimeField()

    def __str__(self):
        return self.title
