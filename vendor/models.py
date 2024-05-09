from django.db import models
from .mixins import TimeStampFields
from django.utils.timezone import now

# Create your models here.

class VendorManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)



class Vendor(TimeStampFields):
    name = models.CharField(max_length=200)
    vcontact = models.CharField(max_length=12)
    vaddress = models.TextField()
    vendor_code = models.CharField(unique=True,max_length=6)
    on_time_delivery_rate = models.DecimalField(max_digits=5,decimal_places = 2, default="00.00" )
    quality_rating_avg = models.DecimalField(max_digits=5,decimal_places = 2, default="00.00" )
    average_response_time = models.DecimalField(max_digits=5,decimal_places = 2, default="00.00" )
    fulfillment_rate = models.DecimalField(max_digits=5,decimal_places = 2, default="00.00" )
    deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    objects = models.Manager() 
    vendor_objects = VendorManager()
       

class HistoricalPerformance(TimeStampFields):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    date = models.DateTimeField(default=now)
    on_time_delivery_rate =  models.DecimalField(max_digits=5,decimal_places = 2, default="00.00" )
    quality_rating_avg = models.DecimalField(max_digits=5,decimal_places = 2, default="00.00" )
    average_response_time = models.DecimalField(max_digits=5,decimal_places = 2, default="00.00" )
    fulfillment_rate = models.DecimalField(max_digits=5,decimal_places = 2, default="00.00" )

   










