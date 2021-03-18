  
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *




class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"


class Usersserializer(serializers.ModelSerializer):
   
    class Meta:
        model=Profile
        fields="__all__"