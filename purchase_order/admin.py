from django.contrib import admin
from .models import PurchaseOrder

# Register your models here.

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display=['po_number','vendor','items','quantity','status','created_at','updated_at','delivery_date','quality_rating','issue_date','acknowledgment_date',]
    fields = ['po_number','vendor','items','quantity','status','delivery_date','quality_rating','issue_date','acknowledgment_date']
    list_filter = ['vendor']
