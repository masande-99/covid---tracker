from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ResultsForm

# Create your views here.

def home(request):
    results = Results.objects.all()

    # results1 = Results.objects.all()
    totalresults = results.count()

    departments = results.filter(department='Quality Assurance').count()
    departments1 = results.filter(department='Data Team').count()
    departments2 = results.filter(department='Development').count()


    context = {'results': results, 'totalresults': totalresults,
               'departments': departments, 'departments1': departments1,
               'departments2': departments2}

    return render(request, 'app/dashboard.html', context)


def products(request):
    results = Results.objects.all()

    # results1 = Results.objects.all()
    totalresults = results.count()

    departments = results.filter(department='Quality Assurance').count()
    departments1 = results.filter(department='Data Team').count()
    departments2 = results.filter(department='Development').count()

    context = {'results': results, 'totalresults': totalresults,
               'departments': departments, 'departments1': departments1,
               'departments2': departments2}

    return render(request, 'app/products.html', context)


def customer(request):
    return render(request, 'app/customer.html')


def covidTrackerForm(request):
    form = ResultsForm()
    if request.method == 'POST':
        form = ResultsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/results/')

    context = {'form':form}
    return render(request, 'app/form.html', context)

def QA_records(request):
    results = Results.objects.all()

    QA_department = results.filter(department='Quality Assurance')

    context = {'QA_department': QA_department}

    return render(request, 'app/QA_team_records.html', context)

def Data_team_records(request):
    results = Results.objects.all()

    Data_team_department = results.filter(department='Data Team')

    context = {'Data_team_department': Data_team_department,}

    return render(request, 'app/Data_team_records.html', context)

def Development_records(request):
    results = Results.objects.all()

    Development_department = results.filter(department='Development')

    context = {'Development_department': Development_department}

    return render(request, 'app/Development_records.html', context)
