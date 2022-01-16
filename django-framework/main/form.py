from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field, Submit, HTML
from django import forms




class JourneyForm(forms.Form):
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class' : "formTextField"}))

    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class' : "formTextField"}))

    start_time = forms.TimeField(
        label='Start Time', widget=forms.TimeInput(attrs={'placeholder':"Selected time", 'type':"time",
                                                     'id':"appt", 'class' : "formTextField"}))
    end_time = forms.TimeField(
        label='End Time', widget=forms.TimeInput(attrs={'placeholder':"Selected time", 'type':"time",
                                                     'id':"appt", 'class' : "formTextField"}))

    plate_number=forms.CharField(max_length=128, widget=forms.TextInput(attrs={
        'type':'text1', 'class':"form-control formTextField", 'placeholder':'Type in Manually'
    }))

    driver = forms.CharField(
        max_length=128,  widget=forms.TextInput(
            attrs={'placeholder':"Name", 'class':"form-control formTextField", 'type':'text1', "id":'driver_name'}))

    CHOICES=(('1', 'Transport of goods'),('2','Picking up of goods'), ('3','Transport of people'),
            ('4','Fieldwork'))
    purpose = forms.CharField(widget=forms.Select(choices=CHOICES,
                              attrs={'class':"form-select formTextField", "aria-label":'Default select example'}))

    no_of_pass = forms.IntegerField(min_value=1,max_value=8,widget=forms.NumberInput(attrs={'class':"formTextField"}))

    destinations=forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class':"formTextField",
                                                                              'label': 'Destination of The Trip'}))
    mileage_start=forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class':"formTextField",
                                                                              'label': 'Mileage Start Number',
                                                                            'placeholder':'Enter start value'}))
    mileage_finish = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': "formTextField",
                                                                      'label': 'Mileage End Number',
                                                                        'placeholder':'Enter end value',
                                                                        }))
    is_round_trip=forms.BooleanField(required=False,
                                     widget=forms.CheckboxInput(
                                         attrs={'label':'Is round Trip',
                                                'placeholder':'Is yes, please tick it'}))
    #fuel_liter=forms.FloatField(widget=forms.NumberInput(attrs={'label':'Fuel Liter',
                                                                #"placeholder": 'Please type in float number'}))
    approved_status=forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(JourneyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = "col-md-2"
        self.helper.layout = Layout(

            Fieldset('Date&Time', 'start_date', 'end_date', 'start_time', 'end_time'),
            Fieldset('Vehicle Information','plate_number', 'mileage_start', 'mileage_finish'),
            Fieldset('Journey Information', 'driver', 'purpose', 'no_of_pass', 'destinations',
                     Field('is_round_trip',css_id='tickbox')),
            Field('approved_status')
        )
        self.helper.add_input(Submit('submit', 'Submit', css_id='submitButton'))
        self.helper.form_method = 'POST'
