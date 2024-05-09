from django.urls import path
from .views import *

urlpatterns = [
    path("",FetchPurchaseOrder.as_view(),name="FetchPurchaseOrder"),
    path("<int:id>", PurchaseOrderWithId.as_view(), name="PurchaseOrderWithId"),
    path("<int:id>/acknowledge" , PurchaseOrderWithId.as_view(), name="PurchaseOrderWithId")
]