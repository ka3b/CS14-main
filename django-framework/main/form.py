from django import forms

class JourneyForm(forms.Form):
    date = forms.DateField(auto_now=False, auto_now_add=False)
    driver = forms.CharField(max_length=128, unique=False)
    destination = forms.CharField(max_length=128, unique=False)
    purpose = forms.CharField(max_length=50, unique=False)
    no_of_pass = forms.IntegerField()
    start_time = forms.TimeField(auto_now=False, auto_now_add=False)
    end_time = forms.TimeField(auto_now=False, auto_now_add=False)
    speedo_start = forms.IntegerField()
    speedo_finish = forms.IntegerField()