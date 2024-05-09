from django.shortcuts import render,HttpResponse
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from vendor.models import Vendor
from vendor.serializers import VendorSerializers
from utils.utils import calculate_average
from django.db.models import Sum
from datetime import time, timedelta 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Create your views here.

def on_time_deliveries(id):
    ontime = 0
    purords = PurchaseOrder.objects.filter(status='completed',vendor=id)
    total_completed = len(purords)
    for purord in purords:
        if purord.delivery_date == purord.acknowledgment_date:
            ontime += 1
    rate_percentage = calculate_average(ontime,total_completed)
    return rate_percentage

def quality_rating_average(id):
    vendor_quality_rating = PurchaseOrder.objects.filter(status='completed',vendor=id).aggregate(Sum('quality_rating'))
    total_quality_rating = PurchaseOrder.objects.filter(status='completed',vendor=id).count()
    total_quality_rating = total_quality_rating * 100
    rate_percentage = calculate_average(vendor_quality_rating['quality_rating__sum'],total_quality_rating)
    return rate_percentage    

def average_response_time(id):
    totaltimediff = 0
    purords = PurchaseOrder.objects.filter(status='completed',vendor=id)
    total_completed = len(purords)
    total_completed_seconds = timedelta(days = total_completed).total_seconds() * 100
    for purord in purords:
        timediff =  purord.acknowledgment_date - purord.issue_date
        timediff_sec = int(timediff.total_seconds())
        totaltimediff += timediff_sec
    rate_percentage = calculate_average(totaltimediff,total_completed_seconds)  
    return rate_percentage

def fulfillment_rate(id):
    total_completed = PurchaseOrder.objects.filter(status='completed',vendor=id).count()   
    total_canceled = PurchaseOrder.objects.filter(status='canceled',vendor=id).count()  
    rate_percentage = calculate_average(total_completed,total_canceled) 
    return rate_percentage 


class FetchPurchaseOrder(APIView):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]

    def get(self,request, *args, **kwargs):
        purchase_order = PurchaseOrder.purchase_order_objects.all()
        serializered_data = PurchaseOrderSerializer(purchase_order,many=True)
        return Response(serializered_data.data,status=status.HTTP_200_OK)


    def post(self,request,*args,**kwargs):
        serialised_data = PurchaseOrderSerializer(data=request.data)
        if serialised_data.is_valid():
            serialised_data.save()
            return Response(serialised_data.data,status=status.HTTP_201_CREATED)
        return Response({"error":serialised_data.errors},status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrderWithId(APIView):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]


    def get(self,request,*args,**kwargs):
        id = kwargs['id']
        try:
            purchase_order = PurchaseOrder.purchase_order_objects.get(id=id)
            if purchase_order:
                serializered_data = PurchaseOrderSerializer(purchase_order)
                return Response(serializered_data.data,status=status.HTTP_200_OK)
            return Response({"error":"not exist"},status=status.HTTP_400_BAD_REQUEST)     
        except PurchaseOrder.DoesNotExist:
            return Response({"error":"not exist"},status=status.HTTP_400_BAD_REQUEST) 
        
    def patch(self,request, *args , **kwargs):
        id = kwargs['id']
        print("request data====", request.data)
        acknowledgment_date = request.data.get('acknowledgment_date')
        print("acknowledgment_date=====", acknowledgment_date)
        purchase_order = PurchaseOrder.purchase_order_objects.get(id=id)
        if purchase_order:
            serializered_data = PurchaseOrderSerializer(purchase_order, data=request.data,partial=True)
            if serializered_data.is_valid():
                serializered_data.save()
                return Response({"message":"acknowledgment date updated"},status=status.HTTP_200_OK)
            return Response({"error":serializered_data.errors},status=status.HTTP_400_BAD_REQUEST)
        return Response({"error":"not a valid data"},status=status.HTTP_400_BAD_REQUEST)   





    def put(self, request, *args , **kwargs):
        id = kwargs['id']
        purchase_order = PurchaseOrder.purchase_order_objects.get(id=id)
        if purchase_order:
                serializered_data = PurchaseOrderSerializer(purchase_order, data= request.data)
                if serializered_data.is_valid():
                    serializered_data.save()
                    return Response(serializered_data.data,status=status.HTTP_201_CREATED)
                return Response({"error":serializered_data.errors},status=status.HTTP_400_BAD_REQUEST)      
        return Response({"error":"not valid data"},status=status.HTTP_400_BAD_REQUEST)   


    def delete(self, request, *args, **kwargs):
        id = kwargs['id']
        purchase_order = PurchaseOrder.purchase_order_objects.get(id=id)
        if purchase_order:
            purchase_order.deleted = True
            purchase_order.save()
            return Response({"id":id,"message":"deleted"},status=status.HTTP_200_OK)  























