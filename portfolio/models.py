from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True, null=True)
    technologies = models.TextField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile/')
    location = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    github_link = models.URLField(max_length=50)
    linkedin = models.URLField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
