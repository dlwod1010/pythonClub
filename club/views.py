from django.shortcuts import get_object_or_404, render
from .models import meeting, meetingMinutes, resource, event
from .forms import meetingForm, resourceForm

def index(request):
    return render(request, 'club/index.html')


def getresources(request):
    resource_list = resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})


def getmeetings(request):
    meeting_list = meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list': meeting_list})


def getevents(request):
    event_list = event.objects.all()
    return render(request, 'club/events.html', {'event_list': event_list})


def meetingdetails(request, id):
    meetingpk = get_object_or_404(meeting, pk=id)
    minutes = meetingMinutes.objects.filter(meeting=id)
    context = {
        'meetingpk': meetingpk,
        'minutes': minutes,
    }
    return render(request, 'club/meetingdetails.html', context=context)


# def eventdetails(request, )

def newMeeting(request):
    form = meetingForm
    if request.method == 'POST':
        form = meetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = meetingForm()
    else:
        form = meetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

def newResource(request):
    form = resourceForm
    if request.method == 'POST':
        form = resourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = resourceForm()
    else:
        form = resourceForm()
    return render(request, 'club/newresource.html', {'form': form})