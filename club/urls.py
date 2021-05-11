from django.urls import path
from . import views

# Only the index file can use empty quotes for the initial path statement.
urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.getresources, name='resource'),
    path('meetings/', views.getmeetings, name='meeting'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
]
