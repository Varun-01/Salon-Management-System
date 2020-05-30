from django.db import models
import csv
from datetime import datetime  
from django.utils.timezone import now
#from products.models import Product

from django.http import HttpResponse

#
#def export_to_csv(request):
#    response = HttpResponse(content_type='text/csv')
#    response['Content-Disposition'] = 'attachment; filename="mytest.csv"'

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    customer_contact = models.IntegerField(default=0)
    customer_address = models.CharField(max_length=200)
    def __str__(self):
        return self.customer_name

class Staff(models.Model):
    staff_id = models.CharField(primary_key=True, max_length=10000)
    staff_name = models.CharField(max_length=200)
    staff_contact = models.IntegerField(default=0)
    staff_address = models.CharField(max_length=200)
    def __str__(self):
        return self.staff_name
    
class Services(models.Model):
    service_id = models.CharField(primary_key=True, max_length=10000)
    service_name = models.CharField(max_length=200)
    service_category = models.CharField(max_length=200)
    service_cost = models.IntegerField(default=0)
    def __str__(self):
        return self.service_name

class Bill(models.Model):
    bill_number = models.AutoField(primary_key=True)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    staff_name = models.ForeignKey(Staff, on_delete=models.CASCADE, null=False)
    service_name = models.ForeignKey(Services, on_delete=models.CASCADE, null=False)
#    service_amount = models.ForeignObject()
    bill_date = models.DateTimeField((u"Bill date"),default=now, blank=True)
    def __str__(self):
        return str(self.bill_number)
