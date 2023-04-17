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

    start_date = DateField(widget=SelectDateWidget())
    end_date = DateField(widget=SelectDateWidget())
    location = ChoiceField(choices=location_choices)
        