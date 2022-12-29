from django import forms



class EventForm(forms.Form):
    Party_Type = forms.CharField( max_length=50)
    City = forms.CharField(max_length=50)