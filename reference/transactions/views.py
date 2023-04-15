from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .app_forms.forms import AddForm
from .models import Transactions

# Create your views here.
def index(request):
    print(Transactions.type_choices)
    return render(request, 'transactions/index.html')

def add(request):
    if request.method == 'GET':
        form = AddForm()
        print(form.fields)
        return render(request, 'transactions/add.html', {
            'form': form,
        })
    
    if request.method == "POST":
        return HttpResponse('Add POST')