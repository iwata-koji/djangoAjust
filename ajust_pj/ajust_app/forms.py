from django import forms
from .models import Event, Date, Participant, Response

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title']

class DateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name']

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['availability']