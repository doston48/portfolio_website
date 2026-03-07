from django.shortcuts import render, get_object_or_404
from .models import Project, Profile

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "portfolio/project_detail.html", {'project': project})

def profile(request):
    profile = profile.objects.first()
    return render(request,'portfolio/profile.html',{'profile': profile})