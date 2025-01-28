from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
import logging
from .models import Student

# Create your views here.

logger=logging.getLogger('django')

class FirstApiTestView(APIView):
        
        authentication_class=[]
        permission_class=[]

        def get(self,request):
            try:
                data=[]

                # retrieve all objects
                # students=Student.objects.all()

                # retrieve only selected parts
                students=Student.objects.filter(age=9)

                for student in students:
                     data.append({
                          "name":student.name,
                          "address":student.address,
                          "age":student.age,
                          "mobile_number":student.mobile_number
                     })
                msg={
                        "response":"success",
                        "data":data
                }
                return Response(msg,status=status.HTTP_200_OK)
            except Exception as e:
                 logger.info(str(e),exc_info=True)
                 msg={
                      "response":"fail"
                 }
                 return Response(msg,status=status.HTTP_400_BAD_REQUEST)
        

