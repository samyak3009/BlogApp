from email import message
import imp
from re import L
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapi import serializers
from rest_framework import viewsets
from myapi import models

class HelloApiView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        an_apiview = [
            "anshay",
            "samyak",
            "harshita",
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self,request,pk=None):
        """Handling updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handling partial update of an object"""
        return Response({'method': 'Patch'})

    def delete(self, request, pk=None):
        return Response({'method': 'delete'})

class HelloViewSets(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            "rastogi",
            "jain",
            "sachdeva",
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """handling partial update of an object"""
        return Response({'http_method': 'Patch'})

    def partial_update(self, request, pk=None):
        """handling partial update of an object"""
        return Response({'http_method': 'Put'})    
    
    def destroy(self, request, pk=None):
        """handling partial update of an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    