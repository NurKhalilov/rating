from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import RateAddForm
from django.http import HttpResponse
from .utils import json_maker, average_values, get_plot
import pandas as pd
from .models import Region


def dashboard(request):
    regions = Region.objects.all()
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard',
                   'regions': regions})


def report_add(request, region_id):
    print(region_id)
    form = RateAddForm(region_id=region_id)
    if request.method == 'POST':
        form = RateAddForm(request.POST)
        if form.is_valid():
            message = "Thanks!"
            form.save()
            return redirect('http://127.0.0.1:8000/survey/1/')
        else:
            print("Something went wrong!")
            form = RateAddForm(request.POST, region_id=region_id)
    return render(request,
                  'account/report.html',
                  {'form': form})


def average_show(request):
    average = average_values()
    return render(request,
                  'report/table.html',
                  {'average': average})
    

def json(request):
    data = json_maker()
    return render(request,
                  'report/report.html',
                  {'data': data})


def graph_show(request):
    new_data = average_values()
    x = [new_data[i]['salesperson'] for i in range(len(new_data))]
    y = [new_data[i]['average'] for i in range(len(new_data))]
    
    data = json_maker()
    df = pd.read_json(data)
    df = df.set_index('id')
    z = df['salesperson'].value_counts(sort=False)
    
    chart = get_plot(x,y,z)
    return render(request,
                  'report/graph.html',
                  {'chart': chart})
    