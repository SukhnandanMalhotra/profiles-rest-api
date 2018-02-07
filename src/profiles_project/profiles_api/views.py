from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from . import serializers
from . import models
from . import permissions


# Create your views here.
class HelloAPIView(APIView):
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        an_apiview = [
        'Uses Http methods as function(get,post,patch,put,delete)',
        'It is similar to a traditional Django View',
        'Gives you the most control over your logic',
        'Is mapped manually to URLS'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self,request):
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        return Response({'method':'delete'})

class UserProfileViewset(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
