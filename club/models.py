from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class meeting(models.Model):
    meetingTitle = models.CharField(max_length=255)
    meetingDate = models.DateField()
    meetingTime = models.TimeField()
    meetingLocationAt = models.CharField(max_length=255)
    meetingAgenda = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.meetingTitle

    class Meta:
        db_table = 'meeting'
        verbose_name_plural = 'meetings'


class meetingMinutes(models.Model):
    meeting = models.ForeignKey(meeting, on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minutesText = models.TextField()

    def __str__(self):
        return self.minutesText

    class Meta:
        db_table = 'meetingMinute'
        verbose_name_plural = 'meetingMinutes'


class resource(models.Model):
    resourceName = models.CharField(max_length=255)
    resourceType = models.CharField(max_length=255)
    resourceUrl = models.URLField()
    dateEntered = models.DateField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField()

    def __str__(self):
        return self.resourceName

    class Meta:
        db_table = 'resource'
        verbose_name_plural = 'resources'


class event(models.Model):
    eventTitle = models.CharField(max_length=255)
    eventLocation = models.CharField(max_length=255)
    eventDate = models.DateField()
    eventTime = models.TimeField()
    eventDescription = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventTitle

    class Meta:
        db_table = 'event'
        verbose_name_plural = 'events'
