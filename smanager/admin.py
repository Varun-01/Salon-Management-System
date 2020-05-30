from django.contrib import admin
from .models import Customer
from .models import Staff
from .models import Services
from .models import Bill
from django.shortcuts import render
# Register your models here.

admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(Services)
admin.site.register(Bill)
admin.site.index_template = 'personal/page1.html'
admin.autodiscover()