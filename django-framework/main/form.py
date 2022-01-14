from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field, Submit, HTML
from django import forms




class JourneyForm(forms.Form):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class' : "formTextField"}))

    start_time = forms.TimeField(
        label='Start Time', widget=forms.TimeInput(attrs={'placeholder':"Selected time", 'type':"time",
                                                     'id':"appt", 'class' : "formTextField"}))
    end_time = forms.TimeField(
        label='End Time', widget=forms.TimeInput(attrs={'placeholder':"Selected time", 'type':"time",
                                                     'id':"appt", 'class' : "formTextField"}))

    Licenese_No=forms.CharField(max_length=128, widget=forms.TextInput(attrs={
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

    destination=forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class':"formTextField",
                                                                              'label': 'Destination of The Trip'}))
    speedo_start=forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class':"formTextField",
                                                                              'label': 'Speedo Start Number',
                                                                            'placeholder':'Please type integer'}))
    speedo_end = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': "formTextField",
                                                                      'label': 'Speedo End Number',
                                                                        'placeholder':'Please type integer',
                                                                        }))
    is_round_trip=forms.BooleanField(required=False,
                                     widget=forms.CheckboxInput(
                                         attrs={'label':'Is round Trip',
                                                'placeholder':'Is yes, please tick it'}))
    fuel_liter=forms.FloatField(widget=forms.NumberInput(attrs={'label':'Fuel Liter',
                                                                "placeholder": 'Please type in float number'}))
    approved_status=forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(JourneyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = "col-md-2"
        self.helper.layout = Layout(

            Fieldset('Date&Time', 'date','start_time', 'end_time'),
            #HTML("""
                    #<p><strong>Hello, this is a fucking test</strong></p>
                #"""),
            Fieldset('Vehicle Information','Licenese_No', 'speedo_start', 'speedo_end'),
            Fieldset('Journey Information', 'driver', 'purpose', 'no_of_pass', 'destination',
                     Field('is_round_trip',css_id='tickbox')),
            Field('approved_status')
        )
        self.helper.add_input(Submit('submit', 'Submit', css_id='submitButton'))
        self.helper.form_method = 'POST'