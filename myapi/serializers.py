from dataclasses import field
from rest_framework import serializers
from myapi import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.UserProfile
        fields=('id', 'email', 'name', 'password')
        extra_kwargs={
            'password':{
                'write_only': True,
                'style': {'input_type':'password'}
            }
        }
    def create(self, validated_data):
        """Create and return a new user"""
        user=models.UserProfile.objects.create_user( #overriding the create function, create_user() is defined in UserProfilemanager
            email = validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
    
    def update(self, instance, validated_data):
        """Handling updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
            
        return super().update(instance, validated_data)