from django.shortcuts import render
import requests
from django.db.models import Count, Q
from django.shortcuts import render

def home(request):
    return render(request, 'D:/ACE/BE PROJECT/DJANGO FINAL/salon/smanager/templates/personal/header.html')
def reports(request):
    return render(request, 'D:/ACE/BE PROJECT/DJANGO FINAL/salon/smanager/templates/personal/reports.html')
