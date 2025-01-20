from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.
class LoginAPIView(APIView):
    @swagger_auto_schema(
         request_body= openapi.Schema(
                 type = openapi.TYPE_OBJECT,properties={
                     "username":openapi.Schema(title = "password",type = openapi.TYPE_STRING,),
                     "password":openapi.Schema(title = "password",type = openapi.TYPE_STRING,),
                 },
            required = ["username","password"],
         )
    )
               
             
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username == "" and password == "":
            return Response({
                "detail": "Fields are empty"
            
            })
        user = authenticate(username = username,password = password)
        if user:
            token,_= Token.objects.get_or_create(user= user)
            return Response({
                "token": token.key,
                "user": username,
                "success": "User logg in"
            })
          
    
    