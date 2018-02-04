from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloAPIView(APIView):

    def get(self,request,format=None):
        an_apiview = [
        'Uses Http methods as function(get,post,patch,put,delete)',
        'It is similar to a traditional Django View',
        'Gives you the most control over your logic',
        'Is mapped manually to URLS'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
