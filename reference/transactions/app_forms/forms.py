from django.forms import ModelForm, Select
from transactions.models import Transactions

class AddForm(ModelForm):
    class Meta:

        model = Transactions
        fields = ['type', 'location', 'format']
        