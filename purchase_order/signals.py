from .models import PurchaseOrder
from vendor.models import Vendor, HistoricalPerformance
from django.db.models.signals import post_save
from django.dispatch import receiver
from .views import *


@receiver(post_save,sender = PurchaseOrder)
def PurchaseOrderUpdateStatus(sender,instance,created,**kwargs):
    if not created:
        vendor_id = instance.vendor.id
        on_time_deliveries_val = on_time_deliveries(vendor_id)
        quality_rating_average_val = quality_rating_average(vendor_id)
        average_response_time_val = average_response_time(vendor_id)
        fulfillment_rate_val = fulfillment_rate(vendor_id)
        vendor = Vendor.objects.get(id=vendor_id)
        if vendor:
            vendor.on_time_delivery_rate = on_time_deliveries_val
            vendor.quality_rating_avg = quality_rating_average_val
            vendor.average_response_time = average_response_time_val
            vendor.fulfillment_rate = fulfillment_rate_val
            vendor.save()
        
        historical_performance = HistoricalPerformance.objects.filter(vendor = vendor_id).count()

        if historical_performance == 1:
            historical_performance_obj = HistoricalPerformance.objects.get(vendor = vendor_id)
            historical_performance_obj.on_time_delivery_rate = on_time_deliveries_val
            historical_performance_obj.quality_rating_avg = quality_rating_average_val
            historical_performance_obj.average_response_time = average_response_time_val
            historical_performance_obj.fulfillment_rate = fulfillment_rate_val
            historical_performance_obj.save()
        else:
            sv = HistoricalPerformance(
                vendor = vendor,
                on_time_delivery_rate = on_time_deliveries_val,
                quality_rating_avg = quality_rating_average_val,
                average_response_time = average_response_time_val,
                fulfillment_rate = fulfillment_rate_val)
            sv.save()    


        print(f"An instance of {sender.__name__} was updated: {instance}")