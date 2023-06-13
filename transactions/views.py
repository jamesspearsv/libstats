from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from .app_forms.forms import AddForm
from .models import Transaction
from .util import alerts
from datetime import datetime


# Create your views here.
def index(request):

    ALLOWED_IPS = ['10.24.20.210']

    # Count total # of recorded transactions in current month and year
    monthlyTransactionCount = Transaction.objects.filter(date__year=datetime.now().year, date__month=datetime.now().month).count()

    # Testing IP Authentication. Could be moved into a decorator function
    print(request.META.get('HTTP_X_FORWARDED_FOR'))
    print(request.META.get('REMOTE_ADDR'))
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if ip not in ALLOWED_IPS:
        return HttpResponse('403: NOT ALLOWED')

    return render(request, 'transactions/index.html', {
        'count': monthlyTransactionCount,
        'ip': ip
    })

def add(request):
    if request.method == 'GET':
        form = AddForm()
        alert = alerts(request)
        return render(request, 'transactions/add.html', {
            'form': form,
            'alert': alert
        })
    
    if request.method == "POST":
        form = AddForm(request.POST)
        
        if form.is_valid():
            # If form is valid save new transaction to model
            form.save()
            return HttpResponseRedirect(f"{reverse('transactions:add')}?s=0")
        
        else:
            return HttpResponseRedirect(f"{reverse('transactions:add')}?e=2")

def view(request):
        
        if request.method == 'POST':

            # Validate form response data. If not valid return an error.
            if not request.POST.get('start_date') or not request.POST.get('end_date'):
                return HttpResponseRedirect(f"{reverse('transactions:view')}?e=0")
            
            elif request.POST.get('end_date') < request.POST.get('start_date'):
                return HttpResponseRedirect(f"{reverse('transactions:view')}?e=1")
            
            else:
                # Store form response data to query database
                start_date = request.POST.get('start_date') #YYYY-MM-DD
                end_date =  request.POST.get('end_date') #YYYY-MM-DD

                results = Transaction.objects.filter(date__gte=start_date, date__lte=end_date)

                return render(request, 'transactions/results.html', {
                    'results': results,
                    'start_date': start_date,
                    'end_date': end_date
                })


        if request.method == 'GET':

            alert = alerts(request)

            return render(request, 'transactions/search.html', {
                'choices': Transaction.location_choices,
                'alert': alert
            })

def reports(request):

    if request.method == 'POST':
        # Validate form response data. If not valid return an error.
        if not request.POST.get('start_date') or not request.POST.get('end_date') or not request.POST.get('location'):
            return HttpResponseRedirect(f"{reverse('transactions:reports')}?e=0")
        elif request.POST.get('end_date') < request.POST.get('start_date'):
            return HttpResponseRedirect(f"{reverse('transactions:reports')}?e=1")
        
        # Else query model and compile report
        else:
            start_date = request.POST['start_date'] #YYYY-MM-DD
            end_date =  request.POST['end_date'] #YYYY-MM-DD
            form_location = request.POST['location']

            # Model: choices[choice][(choice_value, choice_label)]
            # Model: 0 == value, 1 == label
            
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

        alert = alerts(request)

        return render(request, 'transactions/generate.html', {
            'choices': Transaction.location_choices,
            'alert': alert
        })
    
def error404(request, exception=None):
    return render(request, 'transactions/404.html', status=404)

def error500(request, exception=None):
    return render(request, 'transactions/500.html', status=500)
