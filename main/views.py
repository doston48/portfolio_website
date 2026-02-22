from django.shortcuts import render, get_object_or_404
from .models import project

def projects(request):
    projects = project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(project, pk=pk)
    return render(request, "project_detail.html", {'project': project})

def profile(request):
 return render(request, 'profile.html')