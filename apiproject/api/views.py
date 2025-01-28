from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
import logging

# Create your views here.

logger=logging.getLogger('django')

class FirstApiTestView(APIView):
        
        authentication_class=[]
        permission_class=[]

        def get(self,request):
            try:
                msg={
                        "response":"success",
                        "data":[{"name":"Umesh","address":"Bhaktapur"}]
                }
                return Response(msg,status=status.HTTP_200_OK)
            except Exception as e:
                 logger.info(str(e),exc_info=True)
                 msg={
                      "response":"fail"
                 }
                 return Response(msg,status=status.HTTP_400_BAD_REQUEST)
        

