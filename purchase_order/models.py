from django.db import models
from vendor.mixins import TimeStampFields
from vendor.models import Vendor
from datetime import datetime

# Create your models here.

class PurchaseOrderManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class PurchaseOrder(TimeStampFields):
    STATUSES = (
        ('pending' , "Pending"),
        ("completed" , "Completed"),
        ("canceled" , "Canceled")
    )
    po_number = models.IntegerField(default="0",unique = True)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=datetime.now)
    delivery_date = models.DateTimeField(default=datetime.now)
    items = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    status = models.CharField(choices=STATUSES,max_length=200,default='pending')
    quality_rating = models.DecimalField(max_digits = 5, decimal_places=2,default="00.00", null= True)
    issue_date = models.DateTimeField(default=datetime.now)
    acknowledgment_date = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'PO Number : {self.po_number}'

    objects = models.Manager()    

    purchase_order_objects = PurchaseOrderManger()
