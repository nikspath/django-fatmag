from django.contrib import admin
from .models import Vendor ,  HistoricalPerformance

# Register your models here.

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name','vcontact','vaddress', 'vendor_code','created_at','updated_at','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate',]


@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ['vendor','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate',]
    readonly_fields = [field.name for field in HistoricalPerformance._meta.get_fields()]
    def has_add_permission(self, request, obj=None):
        return False


