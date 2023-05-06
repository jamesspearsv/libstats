from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from .app_forms.forms import AddForm
from .models import Transaction


# Create your views here.
def index(request):
    return render(request, 'transactions/index.html')

def add(request):
    if request.method == 'GET':
        form = AddForm()
        
        try:
            request.GET['s']
            alert = [True, 'primary', '<strong>Success!</strong> Transaction recorded successfully']
        except:
            alert = [False, '', '']

        return render(request, 'transactions/add.html', {
            'form': form,
            'alert': alert[0],
            'type': alert[1],
            'message': alert[2]
        })
    
    if request.method == "POST":
        form = AddForm(request.POST)
        
        if form.is_valid():
            # If form is valid save new transaction to model
            form.save()
            return HttpResponseRedirect(f"{reverse('transactions:add')}?s=1")
        
        else:
            return render(request, 'transactions/500.html', status=500)

def view(request):
        
        if request.method == 'POST':

            # Validate form response data. If not valid return an error.
            try: # If form data is valid
                # Store form response data to query database
                start_date = request.POST['start_date'] #YYYY-MM-DD
                end_date =  request.POST['end_date'] #YYYY-MM-DD

                if end_date < start_date:
                    return HttpResponseRedirect(f"{reverse('transactions:view')}?e=1")
                
                # Query model for transactions matching filter
                results = Transaction.objects.filter(date__gte=start_date, date__lte=end_date)

                return render(request, 'transactions/results.html', {
                    'results': results,
                    'start_date': start_date,
                    'end_date': end_date
                })
            
            except: # If form contains invalid data or not data
                return HttpResponseRedirect(f"{reverse('transactions:view')}?e=2")

        if request.method == 'GET':

            try:
                request.GET['e']
                alert = [True, 'danger', '<strong>Error:</strong> Please submit a valid start date and end date range.']
            except:
                alert = [False, '', '']

            return render(request, 'transactions/search.html', {
                'choices': Transaction.location_choices,
                'alert': alert[0],
                'type': alert[1],
                'message': alert[2]
            })

def reports(request):

    if request.method == 'POST':
        # Validate form response data. If not valid return an error.
        if request.POST['start_date'] == "" or request.POST['end_date'] == "" or request.POST['location'] == "":
            return render(request, 'transactions/500.html', status=500)

        start_date = request.POST['start_date'] #YYYY-MM-DD
        end_date =  request.POST['end_date'] #YYYY-MM-DD
        form_location = request.POST['location']

        # Model: choices[x][x] == choices[value][label]
        
        type_report_data = {}
        format_report_data = {}

        # Get data for type report
        for i in range(len(Transaction.type_choices)):
            key = Transaction.type_choices[i][1]
            value = Transaction.objects.filter(date__gte=start_date, date__lte=end_date, location=form_location, type=Transaction.type_choices[i][0]).count()

            type_report_data[key] = value

        # Get data for format report
        for i in range(len(Transaction.format_choices)):
            key = Transaction.format_choices[i][1]
            value = Transaction.objects.filter(date__gte=start_date, date__lte=end_date, location=form_location, format=Transaction.format_choices[i][0]).count()

            format_report_data[key] = value

        return render(request, 'transactions/reports.html', {
            'start_date': start_date, 
            'end_date': end_date, 
            'location': form_location.capitalize(),
            'type_data': type_report_data,
            'format_data': format_report_data 
        })

    if request.method == 'GET':
        return render(request, 'transactions/generate.html', {
            'choices': Transaction.location_choices
        })
    
def error404(request, exception=None):
    return render(request, 'transactions/404.html', status=404)

def error500(request, exception=None):
    return render(request, 'transactions/500.html', status=500)
