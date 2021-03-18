from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    address=models.CharField( max_length=500,blank=False)
    address2=models.CharField( max_length=500,blank=True)
    
    