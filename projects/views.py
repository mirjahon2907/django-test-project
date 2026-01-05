from django.shortcuts import render

from projects.models import Project




def projects(request):
    projects = Project.objects.all()
    return render(request, 'users/projects.html', {'projects': projects})