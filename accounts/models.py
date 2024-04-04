from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profiles(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date = models.DateField()
    phone = models.CharField(max_length=15)