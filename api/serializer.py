  
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *






class Usersserializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=["address","address2","id"]



class Userserializer(serializers.ModelSerializer):
    users=Usersserializer(many=True,read_only=True)
    class Meta:
        model=User
        fields=["first_name","last_name","id","email","users"]