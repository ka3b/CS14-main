from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field, Submit, HTML
from .models import Purpose
from django import forms




class JourneyForm(forms.Form):
    start_date = forms.DateField(
        label='Start date',
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class' : "formTextField formButton",
                                              }))

    end_date = forms.DateField(
        label='End date',
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class' : "formTextField formButton"}))

    start_time = forms.TimeField(
        label='Start time', widget=forms.TimeInput(attrs={'type':"time",
                                                      'class' : "formTextField formButton"}))
    end_time = forms.TimeField(
        label='End time', widget=forms.TimeInput(attrs={'type':"time",
                                                      'class' : "formTextField formButton"}))

    plate_number=forms.CharField(label='',max_length=128, widget=forms.TextInput(attrs={
        'type':'text1', 'class':"formTextField formButton", 'placeholder':'License Plate'
    }))

    driver = forms.CharField(
        label="",
        max_length=128,  widget=forms.TextInput(
            attrs={'placeholder':"Driver Name", 'class':"form-control formTextField formButton", 'type':'text1',
                   "id":'driver_name'}))

    purposes = Purpose.objects.all()
    CHOICES=[]
    for i in range(purposes.count()):
        CHOICES.append((purposes[i].purpose,purposes[i].purpose))
    purpose = forms.CharField(label='',widget=forms.Select(choices=CHOICES,
                              attrs={'class':"form-select formTextField dropdown formButton", "aria-label":'Default select example'
                                     ,'placeholder':'Journey Purpose'}))

    no_of_pass = forms.IntegerField(label='',min_value=1,max_value=8,widget=forms.NumberInput(attrs={
        'class':"formTextField formButton", 'placeholder':'Number of Passengers'}))

    start_location=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'formTextField formButton',
                                                                           'placeholder':'Starting Location'}))


    destinations1 = forms.CharField(required=True,label='',max_length=256,
                                  widget=forms.TextInput(attrs={'class':"formTextField formButton",
                                                'placeholder': 'Destination'}))
    destinations2 = forms.CharField(required=False,label='', max_length=256,
                                    widget=forms.TextInput(attrs={'class': "formTextField formButton",
                                                'placeholder': 'Second Destination (Optional)', 'id':'dest2'}))
    destinations3 = forms.CharField(required=False, label='', max_length=256,
                                    widget=forms.TextInput(attrs={'class': "formTextField formButton",'id':'dest3',
                                                'placeholder': 'Third Destination (Optional)'}))
    mileage_start=forms.IntegerField(label='',min_value=0, widget=forms.NumberInput(
                                    attrs={'class':"formTextField formButton",
                                                    'label': 'Mileage Start Number',
                                                    'placeholder':'Mileage Start Reading'}))
    mileage_finish = forms.IntegerField(label='',min_value=0, widget=forms.NumberInput(
                                    attrs={'class': "formTextField formButton",
                                                    'label': 'Mileage End Number',
                                                    'placeholder':'Mileage End Reading',
                                                    }))


    Trip_CHOICES = ((True, 'Round Trip'), (False, 'One-Way Trip'))

    is_round_trip = forms.BooleanField(required=False, label="",
                                     widget=forms.RadioSelect(
                                         choices=Trip_CHOICES, attrs={'id':'div_id_is_round_trip'}))

    approved_status=forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput())



    def __init__(self, *args, **kwargs):
        super(JourneyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = "col-md-2"
        self.helper.layout = Layout(


            Div(HTML('''
                    <span class="material-icons-outlined" style="font-size:32px; margin:0; margin-top:50px;">badge</span>
                    <h3 style="display: inline; font-size:32px; margin-bottom:20px" id="override" class="col">Driver Information</h3>
                    '''), 'driver'),
            Div(HTML('''<span class="material-icons-outlined" style="font-size:32px; margin:0; margin-top:50px;">today</span>
                <h3 style="display: inline; font-size:32px;" id="override" class="col">Date and Time</h3>'''), 'start_date', 'end_date', 'start_time', 'end_time'),
            Div(HTML('''<span class="material-icons-outlined" style="font-size:32px; margin:0; margin-top:50px;">directions_car</span>
            <h3 style="display: inline; font-size:32px;" id="override" class="col">Vehicle Information</h3>'''),'plate_number', 'mileage_start', 'mileage_finish'),
            Div(HTML('''<span class="material-icons-outlined" style="font-size:32px; margin:0; margin-top:50px;">explore</span>
            <h3 style="display: inline; font-size:32px;" id="override" class="col">Journey Information</h3>
            '''),
                Field('is_round_trip',css_id='tickbox'), 'start_location',
                  'destinations1', 'destinations2', 'destinations3','no_of_pass','purpose'),
            Field('approved_status')
        )
        self.helper.add_input(Submit('submit', 'Submit', css_id='submitButton'))
        self.helper.form_method = 'POST'

    def clean(self):
        cleaned_data =super().clean()
        end_date=cleaned_data.get('end_date')
        start_date=cleaned_data.get('start_date')
        start_time=cleaned_data.get('start_time')
        end_time=cleaned_data.get('end_time')
        if end_date<start_date:
            msg="Start date must earlier than end date!"
            self.add_error('end_date',msg)
        elif start_date==end_date and end_time<start_time:
            msg='End time is before start time!'
            self.add_error('end_time',msg)

        locationUpperT=['start_location','destinations1','destinations2','destinations3']
        for i in locationUpperT:
            if self.cleaned_data[i]:
                x=len(self.cleaned_data[i])
                self.cleaned_data[i] = (self.cleaned_data[i])[0].upper()+(self.cleaned_data[i])[1-x:].lower()
                print(self.cleaned_data[i])

        return self.cleaned_data






