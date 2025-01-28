from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,TokenAuthentication

# Create your views here.

class FirstApiTestView(APIView):
        
        authentication_class=[]
        permission_class=[]

        def get(self,request):
                msg={
                        "response":"success",
                        "data":[{"name":"Umesh","address":"Bhaktapur"}]
                }
                return Response(msg,status=status.HTTP_200_OK)
        

