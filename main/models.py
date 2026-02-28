from django.db import models

class Project(models.Model):
title = models.CharField(max_length=100)
description = models. TextField()
image = models. ImageField(upload_to='projects/')
github_link = models.URLField(blank=True, null=True)
technologies = models.TextField(blank=True,null-True)
live_link = models.URLField(blank=True, null-True)
created_at = models.DateTimeField(auto_now_add=True)

def _str_(self):
    return self.title 
class