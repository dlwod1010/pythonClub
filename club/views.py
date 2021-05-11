from django.shortcuts import render
from .models import meeting, meetingMinutes, resource, event


def index(request):
    return render(request, 'club/index.html')


def getresources(request):
    resource_list = resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})
