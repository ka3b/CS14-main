from django import forms
from django.utils.safestring import mark_safe


class JourneyForm(forms.Form):

    start_time = forms.TimeField(
        label='Start', widget=forms.TextInput(attrs={
        'type':"datetime-local" , 'class' : "formTextField"}))
    end_time = forms.TimeField(label='End',widget=forms.TextInput(attrs={
        'type':"datetime-local" , 'class' : "formTextField"}))


    destination = forms.CharField(max_length=128)

    driver = forms.CharField(
        max_length=128,  widget=forms.TextInput(
            attrs={'placeholder':"Name", 'class':"form-control formTextField", 'type':'text1', "id":'driver_name'}))

    CHOICES=(('Transport of goods', '1'),('Picking up of goods','2'), ('Transport of people','3'),
            ('Fieldwork','4'))
    purpose = forms.CharField(widget=forms.Select(choices=CHOICES,
                              attrs={'class':"form-select formTextField", "aria-label":'Default select example'}))

    no_of_pass = forms.IntegerField()