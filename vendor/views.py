from django.shortcuts import render
from .models import Vendor,HistoricalPerformance
from django.http import JsonResponse
from .serializers import VendorSerializers, HistoricalPerformanceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# 94642880eafb20cc1a1899ace4af7c00cb9c7b2d

class FetchVendors(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_view_name(self):
        return "Vendor"

    def get(self,request, format=None):
        vendors = Vendor.objects.filter(deleted = False)
        serialised_data = VendorSerializers(vendors,many=True)
        return Response(serialised_data.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializered_data = VendorSerializers(data=request.data)   
        if serializered_data.is_valid():
            serializered_data.save()
            return Response(serializered_data.data,status=status.HTTP_201_CREATED)
        return Response(serializered_data.errors,status = status.HTTP_400_BAD_REQUEST)    


class FetchVendorwithID(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        id=kwargs['id']
        vendor = Vendor.objects.filter(pk=id,deleted=False)
        if vendor:
            serialised_data = VendorSerializers(vendor.first())
            return Response(serialised_data.data, status=status.HTTP_200_OK)
        else:
            return Response({"error":"vendor not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,*args,**kwargs):
        id=kwargs['id']
        vendor = Vendor.objects.get(id=id,deleted=False)
        if vendor is not None:
            serializered_data = VendorSerializers(vendor,data=request.data)
            if serializered_data.is_valid():
                serializered_data.save()
                return Response(serializered_data.data,status=status.HTTP_200_OK)
            return Response(serializered_data.errors,status = status.HTTP_400_BAD_REQUEST)
        return Response({"error":"vendor not found"}, status=status.HTTP_404_NOT_FOUND)   

    def delete(self,request,*args,**kwargs):
        id=kwargs['id']
        vendor = Vendor.objects.get(id=id,deleted=False)
        if vendor is not None:
            vendor.deleted = True
            vendor.save()
            return Response({"id":id,"message" : "deleted"},status=status.HTTP_200_OK)



class FetchPerformance(APIView):
    def get(self,request,*args,**kwargs):
        vendor_id = kwargs['id']
        histomrial_performance = HistoricalPerformance.objects.filter(vendor = vendor_id)
        if histomrial_performance is not None:
            serialised_data = HistoricalPerformanceSerializer(histomrial_performance.first())
            return Response(serialised_data.data,status = status.HTTP_200_OK)
        return Response({"error":"vendor not found"}, status=status.HTTP_404_NOT_FOUND)     
        


















