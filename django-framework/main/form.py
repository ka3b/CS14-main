from django import forms

class JourneyForm(forms.Form):
    start_time = forms.TimeField(auto_now=False, auto_now_add=False, attr={})
    end_time = forms.TimeField(auto_now=False, auto_now_add=False)


    destination = forms.CharField(max_length=128, unique=False)

    driver = forms.CharField(
        max_length=128, unique=False, widget=forms.TextInput(
            attrs={'placeholder':"Name", 'class':"form-control formTextField", 'type':'text1', "id":'driver_name'}))

    CHOICES=(('Transport of goods', '1'),('Picking up of goods','2'), ('Transport of people','3'),
            ('Fieldwork','4'))
    purpose = forms.CharField(widget=forms.Select(choices=CHOICES),
                              attr={'class':"form-select formTextField", "aria-label":'Default select example'})

    no_of_pass = forms.IntegerField()

    speedo_start = forms.IntegerField()
    speedo_finish = forms.IntegerField()