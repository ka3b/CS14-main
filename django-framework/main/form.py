from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field, Submit, HTML
from django import forms




class JourneyForm(forms.Form):
    start_date = forms.DateField(
        label='Start date',
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class' : "formTextField",
                                              }))

    end_date = forms.DateField(
        label='End date',
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class' : "formTextField"}))

    start_time = forms.TimeField(
        label='Start time', widget=forms.TimeInput(attrs={'type':"time",
                                                      'class' : "formTextField"}))
    end_time = forms.TimeField(
        label='End time', widget=forms.TimeInput(attrs={'type':"time",
                                                      'class' : "formTextField"}))

    plate_number=forms.CharField(label='',max_length=128, widget=forms.TextInput(attrs={
        'type':'text1', 'class':"form-control formTextField", 'placeholder':'License Plate'
    }))

    driver = forms.CharField(
        label="",
        max_length=128,  widget=forms.TextInput(
            attrs={'placeholder':"Driver Name", 'class':"form-control formTextField", 'type':'text1',
                   "id":'driver_name'}))

    CHOICES=(('Transport of goods', 'Transport of goods'),('Picking up of goods','Picking up of goods'),
             ('Transport of people','Transport of people'),
            ('Fieldwork','Fieldwork'), ('Canceled', 'Canceled'))
    purpose = forms.CharField(label='',widget=forms.Select(choices=CHOICES,
                              attrs={'class':"form-select formTextField", "aria-label":'Default select example'
                                     ,'placeholder':'Journey Purpose'}))

    no_of_pass = forms.IntegerField(label='',min_value=1,max_value=8,widget=forms.NumberInput(attrs={
        'class':"formTextField", 'placeholder':'Number of Passengers'}))

    start_location=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'formTextField',
                                                                           'placeholder':'Starting Location'}))


    destinations1 = forms.CharField(required=True,label='',max_length=256,
                                  widget=forms.TextInput(attrs={'class':"formTextField",
                                                'placeholder': 'Destination'}))
    destinations2 = forms.CharField(required=False,label='', max_length=256,
                                    widget=forms.TextInput(attrs={'class': "formTextField",
                                                'placeholder': 'Second Destination (Optional)', 'id':'dest2'}))
    destinations3 = forms.CharField(required=False, label='', max_length=256,
                                    widget=forms.TextInput(attrs={'class': "formTextField",'id':'dest3',
                                                'placeholder': 'Third Destination (Optional)'}))
    mileage_start=forms.IntegerField(label='',min_value=0, widget=forms.NumberInput(attrs={'class':"formTextField",
                                                                              'label': 'Mileage Start Number',
                                                                            'placeholder':'mileage start reading'}))
    mileage_finish = forms.IntegerField(label='',min_value=0, widget=forms.NumberInput(attrs={'class': "formTextField",
                                                                      'label': 'Mileage End Number',
                                                                        'placeholder':'mileage end reading',
                                                                        }))


    Trip_CHOICES = ((True, 'Round Trip'), (False, 'One-way Trip'))

    is_round_trip = forms.BooleanField(required=False, label="",
                                     widget=forms.RadioSelect(
                                         choices=Trip_CHOICES))

    approved_status=forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(JourneyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = "col-md-2"
        self.helper.layout = Layout(


            Div(HTML('''<span class="material-icons-outlined">badge</span>
                        <h3 style="display: inline">Driver Information</h3>'''), 'driver'),
            Div(HTML('''<span class="material-icons-outlined">today</span>
                <h3 style="display: inline">Date and Time</h3>'''), 'start_date', 'end_date', 'start_time', 'end_time'),
            Div(HTML('''<span class="material-icons-outlined">directions_car</span>
            <h3 style="display: inline">Vehicle Information</h3>'''),'plate_number', 'mileage_start', 'mileage_finish'),
            Div(HTML('''<span class="material-icons-outlined">explore</span>
            <h3 style="display: inline">Journey Information</h3>'''),
                Field('is_round_trip',css_id='tickbox'), 'start_location',
                  'destinations1', 'destinations2', HTML('<br/>'),'destinations3','no_of_pass','purpose'),
            Field('approved_status')
        )
        self.helper.add_input(Submit('submit', 'Submit', css_id='submitButton'))
        self.helper.form_method = 'POST'
