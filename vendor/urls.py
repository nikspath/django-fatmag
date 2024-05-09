from django.urls import path
from .views import *


urlpatterns = [
    path('',FetchVendors.as_view(),name="fetch_vendors"),
    path('<int:id>',FetchVendorwithID.as_view(),name="FetchVendorwithID"),
    path('<int:id>/performance' , FetchPerformance.as_view(), name="FetchPerformance")
]