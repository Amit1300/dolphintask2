from django.urls import path
from .views import UserApi,Userdetails
urlpatterns = [
    path('api/',UserApi.as_view()),
    path('api/<int:pk>',UserApi.as_view()),
    path('userdetails/',Userdetails.as_view()),
    path('userdetails/<int:pk>',Userdetails.as_view()),

]