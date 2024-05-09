from django.shortcuts import render
from django.contrib.auth import authenticate , login
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
import json
# Create your views here.

@csrf_exempt
def login_user(request):
    print(request)
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print("request==",data)
        username = data.get('username')
        password = data.get('password')
        print("username===",username)
        print("password===",password)
        user = authenticate(request, username = username,password = password)
        print("user===",user)
        if user is not None:
            login(request,user)
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'message':"login successfully","token":token.key},status=200)
        else:
            return JsonResponse({'message':"username and password not match"},status=400)
    else:
        return JsonResponse({'message':"method not allowed"},status=405)


