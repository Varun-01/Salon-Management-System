from django.shortcuts import render
from django.http import HttpResponse
from .models import Bill
from django.db.models import Count, Q
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'personal/header.html')

def report1(request):
    dataset = Bill.objects \
        .values('service_name') \
        .annotate(service_count=Count('service_name') \
        .order_by('service_name'))
    return render(request, 'report1.html', {'dataset': dataset})