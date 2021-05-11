from django.forms import ModelForm
from .models import meeting, resource

class meetingForm(ModelForm):
  
    class Meta:
        model = meeting
        fields = ['meetingTitle', 'meetingDate', 'meetingLocationAt', 'meetingAgenda']


class resourceForm(ModelForm):
    
    class Meta:
        model = resource
        fields = '__all__'


