from django import forms
from django.utils.safestring import mark_safe


class JourneyForm(forms.Form):

    start_time = forms.TimeField(
        label='Start', widget=forms.TextInput(attrs={
        'type':"datetime-local" , 'class' : "formTextField"}))
    end_time = forms.TimeField(label='End',widget=forms.TextInput(attrs={
        'type':"datetime-local" , 'class' : "formTextField"}))

    Licenese_No=forms.CharField(max_length=128, widget=forms.TextInput(attrs={
        'type':'text1', 'class':"form-control formTextField", 'placeholder':'Type in Manually'
    }))
    destination = forms.CharField(max_length=128)

    driver = forms.CharField(
        max_length=128,  widget=forms.TextInput(
            attrs={'placeholder':"Name", 'class':"form-control formTextField", 'type':'text1', "id":'driver_name'}))

    CHOICES=(('1', 'Transport of goods'),('2','Picking up of goods'), ('3','Transport of people'),
            ('4','Fieldwork'))
    purpose = forms.CharField(widget=forms.Select(choices=CHOICES,
                              attrs={'class':"form-select formTextField", "aria-label":'Default select example'}))

    no_of_pass = forms.IntegerField()