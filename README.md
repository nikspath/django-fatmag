# FATMUG with django rest framework 
# installation windows:
	-> pip install vertualenv
	virtualenv myenv or python -m virtualenv myenv
	cd myenv
	cd Scripts
	activate
# install django 
-> pip install django
# start project:
  -> django-admin startproject fatmug
# run project:
	-> python manage.py runserver
	-> python manage.py runserver 0.0.0.0:8001
# start app
  -> python manage.py startapp vendor
  -> python manage.py startapp purchase_order
  -> python manage.py startapp auth_user
# create table 
  -> python manage.py makemigrations
  -> python manage.py migrate
# used database
  -> sqlite
# create super user
  -> python manage.py createsuperuser
  -> for this project :
      -> username : admin
      -> password : admin

#######################################################################
# API:

# Purchase order API:

  - GET http://127.0.0.1:8000/api/purchase_order
    -> it will fetch all purchase order list
  - GET http://127.0.0.1:8000/api/purchase_order/1  
    -> This api will fetch single purchase order
  - POST http://127.0.0.1:8000/api/purchase_order/
    -> This is post api which create new purchase order
    -> Example post request body:
    ->  {
          "vendor_id" : 1,
          "po_number": 12434,
          "order_date": "2024-05-08",
          "delivery_date": "2024-05-11",
          "items": "roses",
          "quantity": 2,
          "status": "pending",
          "issue_date": "2024-05-08"
        }
    - PUT http://127.0.0.1:8000/api/purchase_order/5
      -> This api will update your purchase order
      -> Example put request body:
      -> {
          "status": "completed",
          "acknowledgment_date": "2024-05-11",
          "quality_rating": "20.00",
          "vendor_id" : 1,
          "items": "roses"
        }
  - PATCH http://127.0.0.1:8000/api/purchase_order/5/acknowledge
    -> This api will update acknowlwdge date
    -> Example Patch request body:
    -> {    
	      "acknowledgment_date": "2024-05-12"
      }
#############################################################################
# Vendor API
  - GET http://127.0.0.1:8000/api/vendors
     -> This will fetch all list of vendors
  - POST http://127.0.0.1:8000/api/vendors/
    -> This api will create new vendor
    -> Example post request body:
    -> {    
        "name": "test",
        "vcontact": "1234567892",
        "vaddress": "wscc",
        "vendor_code": "23483"
      }
 - GET http://127.0.0.1:8000/api/vendors/11
    -> This api will fetch single vendor
 - PUT http://127.0.0.1:8000/api/vendors/11     
    -> This api will update vendor
    -> Example request put body     
    -> {    
        "name": "nikhil",
        "vcontact": "1234567892",
        "vaddress": "wscc",
        "vendor_code": "23483"
      }

#############################################################################
# authentication :
  -> for all apis I used TokenAuthentication
    ->  authentication_classes = [TokenAuthentication]
        permissions_classes = [IsAuthenticated]
    -> for create token you need to login with username and password
    -> POST http://127.0.0.1:8000/api/auth/login
    -> request body example
    -> {    
        "username" : "admin",
        "password" : "admin"
      }
    -> in response you will get token  
    
#############################################################################
# Code explaination
  # vendor views.py
    -> In this file all business logic 
    -> APIView for rest_frameowrk views
    ->FetchVendors :
        -> this class contain GET and POST function to fetch all vendors and create new vendor
    -> FetchVendorwithID :
        -> this class contain GET and PUT function which fetch individual vendor and update individial vendor
    -> FetchPerformance : 
        -> this class fetch individual vendor performance
# vendor serializers.py
    -> VendorSerializers 
      -> this class serialize Vendor model 
    -> HistoricalPerformanceSerializer
        -> this class serialize HistoricalPerformance model
# vendor models.py
    -> this file contain Vendor and HistoricalPerformance fields to create table
# vendor mixins.py 
    -> this file contain TimeStampFields class which abstract class for all models
    
 # purchase order views.py
    -> In this file all business logic 
    -> APIView for rest_frameowrk views
    ->FetchPurchaseOrder :
        -> this class contain GET and POST function to fetch all purchase order and create new purchase order
    -> PurchaseOrderWithId :
        -> this class contain GET and PUT function which fetch individual purchase order and update individial purchase order
    -> on_time_deliveries : 
        -> this function will give you individual on time delivery average rate 
     -> quality_rating_average : 
        -> this function will give you individual quality rating average rate 
    -> average_response_time : 
        -> this function will give you individual average response time rate     
# vendor serializers.py
    -> PurchaseOrderSerializer 
      -> this class serialize PurchaseOrder model 
    
# vendor models.py
    -> this file contain PurchaseOrder fields to create table
# vendor signals.py 
    -> in this I used post_save signal to update details after  update purchase_order table  
    -> this file contain PurchaseOrderUpdateStatus function which update vendor on_time_delivery_rate,quality_rating_avg, average_response_time, fulfillment_rate
        and also create and update HistoricalPerformance table date for individual vendor

        
# utils utils.py
  -> this file contain calculate_average function which calculate average rate
# auth_user views.py
  -> this file contain login_user which to login with admin user and create token 

#############################################################################  
  
  
      
    
        
          
      
        
