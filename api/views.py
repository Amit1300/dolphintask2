from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer import Usersserializer,Userserializer
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User
from .models import *
from django.core.paginator import Paginator
# Create your views here.
class UserApi(APIView):

    def get(self, request):
        users=Profile.objects.all()
        print(users)
        paginator = Paginator(users, 10)
        serializer=Usersserializer(users, many=True)
        return Response(serializer.data)
        

    def post(self,request):
        users=User.objects.all()
        
        for user in users:
            print(user.id)
            if user.id==request.data["user"]:
                serializer=Usersserializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        users=User.objects.all()
        for user in users:
            if user.id==request.data["user"]:
                serializer=Usersserializer(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Userdetails(APIView):

    def get(self,request):
        users=User.objects.all()
        print(users)
        paginator = Paginator(users, 10)
        serializer=Userserializer(users, many=True)
        return Response(serializer.data)


    def put(self,request,pk):
        user=User.objects.get(pk=pk)
        if user:
            users={}
            users["first_name"]=request.data["first_name"]
            users["last_name"]=request.data["last_name"]
            users["email"]=request.data["email"]
            serializer=Userserializer(user,data=users)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"msg":"error"})