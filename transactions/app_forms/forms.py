from django.forms import ModelForm, Form, DateField, SelectDateWidget, ChoiceField, DateInput
from transactions.models import Transaction

class AddForm(ModelForm):
    class Meta:

        model = Transaction
        fields = ['type', 'location', 'format']

class SearchForm(Form):
    location_choices = (
        ('circulation', 'Circulation'),
        ('reference', 'Reference'),
        ('childrens', 'Childrens')
    )

    start_date = DateField(label='Start Date', widget=SelectDateWidget())
    end_date = DateField(label='End Date', widget=SelectDateWidget())
    location = ChoiceField(label='Location', choices=location_choices)


        