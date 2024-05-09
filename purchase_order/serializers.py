from rest_framework import serializers
from .models import PurchaseOrder
from vendor.serializers import VendorSerializers
from vendor.models import Vendor


class PurchaseOrderSerializer(serializers.ModelSerializer):

    vendor_id = serializers.PrimaryKeyRelatedField(
        queryset=Vendor.objects.all(),
        source='vendor',  
        write_only=True   
    )

    vendor = VendorSerializers(read_only = True)

    class Meta:
        model = PurchaseOrder
        fields = '__all__'