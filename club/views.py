from django.shortcuts import get_object_or_404, render
from .models import meeting, meetingMinutes, resource, event


def index(request):
    return render(request, 'club/index.html')


def getresources(request):
    resource_list = resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})


def getmeetings(request):
    meeting_list = meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list': meeting_list})


def meetingdetails(request, id):
    meetingpk = get_object_or_404(meeting, pk=id)
    minutes = meetingMinutes.objects.filter(meeting=id)
    context = {
        'meetingpk': meetingpk,
        'minutes': minutes,
    }
    return render(request, 'club/meetingdetails.html', context=context)
