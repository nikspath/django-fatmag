from rest_framework import serializers
from .models import Vendor, HistoricalPerformance


class VendorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

    def validate_vcontact(self,value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("please enter 10 digit numeric contact number")
        return value
                

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    vendor = VendorSerializers(read_only = True)

    class Meta:
        model = HistoricalPerformance
        fields = '__all__'