from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field, Submit, HTML
from django import forms




class JourneyForm(forms.Form):
    start_date = forms.DateField(
        label='select start date',
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class' : "formTextField",
                                              }))

    end_date = forms.DateField(
        label='select end date',
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class' : "formTextField"}))

    start_time = forms.TimeField(
        label='Select start time', widget=forms.TimeInput(attrs={'type':"time",
                                                      'class' : "formTextField"}))
    end_time = forms.TimeField(
        label='Select end time', widget=forms.TimeInput(attrs={'type':"time",
                                                      'class' : "formTextField"}))

    plate_number=forms.CharField(label='',max_length=128, widget=forms.TextInput(attrs={
        'type':'text1', 'class':"form-control formTextField", 'placeholder':'License Plate'
    }))

    driver = forms.CharField(
        label="",
        max_length=128,  widget=forms.TextInput(
            attrs={'placeholder':"Drive Name", 'class':"form-control formTextField", 'type':'text1',
                   "id":'driver_name'}))

    CHOICES=(('1', 'Transport of goods'),('2','Picking up of goods'), ('3','Transport of people'),
            ('4','Fieldwork'))
    purpose = forms.CharField(label='',widget=forms.Select(choices=CHOICES,
                              attrs={'class':"form-select formTextField", "aria-label":'Default select example'
                                     ,'placeholder':'Journey Purpose'}))

    no_of_pass = forms.IntegerField(label='',min_value=1,max_value=8,widget=forms.NumberInput(attrs={
        'class':"formTextField", 'placeholder':'Number of Passengers'}))

    destinations=forms.CharField(label='',max_length=256, widget=forms.TextInput(attrs={'class':"formTextField",
                                                                              'placeholder': 'Destination of The Trip'}))
    mileage_start=forms.IntegerField(label='',min_value=0, widget=forms.NumberInput(attrs={'class':"formTextField",
                                                                              'label': 'Mileage Start Number',
                                                                            'placeholder':'mileage start reading'}))
    mileage_finish = forms.IntegerField(label='',min_value=0, widget=forms.NumberInput(attrs={'class': "formTextField",
                                                                      'label': 'Mileage End Number',
                                                                        'placeholder':'mileage end reading',
                                                                        }))


    Trip_CHOICES = ((True, 'Round Trip'), (False, 'One-way Trip'))

    is_round_trip=forms.BooleanField(required=True, label="",
                                     widget=forms.RadioSelect(
                                         choices=Trip_CHOICES))
    #fuel_liter=forms.FloatField(widget=forms.NumberInput(attrs={'label':'Fuel Liter',
                                                                #"placeholder": 'Please type in float number'}))

    approved_status=forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(JourneyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = "col-md-2"
        self.helper.layout = Layout(

            Div(HTML('<h3>Date&Time</h3>'), 'start_date', 'end_date', 'start_time', 'end_time'),
            Div(HTML('<h3>Vehicle Information</h3>'),'plate_number', 'mileage_start', 'mileage_finish'),
            Div(HTML('<h3>Journey Information</h3>'), 'driver', 'purpose', 'no_of_pass', 'destinations',
                     Field('is_round_trip',css_id='tickbox')),
            Field('approved_status')
        )
        self.helper.add_input(Submit('submit', 'Submit', css_id='submitButton'))
        self.helper.form_method = 'POST'
