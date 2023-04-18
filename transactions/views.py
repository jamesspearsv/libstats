from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .app_forms.forms import AddForm, SearchForm
from .models import Transaction

# Create your views here.
def index(request):
    return render(request, 'transactions/index.html')

def add(request):
    if request.method == 'GET':
        form = AddForm()
        print(form.fields)
        return render(request, 'transactions/add.html', {
            'form': form,
        })
    
    if request.method == "POST":
        form = AddForm(request.POST)
        
        if form.is_valid():
            # If form is valid save new transaction to model
            form.save()
            return HttpResponseRedirect(reverse('transactions:add'))
        
        else:
            return HttpResponse('Todo - Error adding transaction')

def view(request):
        
        if request.method == 'POST':
            # Model filter information gathered from user submitted form.

            stat_date = request.POST['start_date'] #YYYY-MM-DD
            end_date =  request.POST['end_date'] #YYYY-MM-DD
            form_location = request.POST['location']

            form = SearchForm(request.POST)
            form.data['location']
            # Query model for transactions matching filter
            results = Transaction.objects.filter(date__gte=stat_date, date__lte=end_date, location = form_location)


            return render(request, 'transactions/results.html', {
                'results': results
            })

        if request.method == 'GET':
            form = SearchForm()

            return render(request, 'transactions/search.html', {
                'form': form,
                'choices': Transaction.location_choices
            })