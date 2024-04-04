from django.db import models
from django.contrib.auth.models import User
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
transprent = os.path.join(BASE_DIR,'static/img/xpg_banner1.png')

# Create your models here.


class developermodel(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    contact= models.CharField(max_length=15)
    gmail= models.CharField(max_length=100)
    desc= models.TextField()

class xprojectmodel(models.Model):
    name= models.CharField(max_length=100)
    category =models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics', blank=True, default="False")
    img3 = models.ImageField(upload_to='pics', blank=True, default="False")
    img4 = models.ImageField(upload_to='pics', blank=True, default="False")
    img5 = models.ImageField(upload_to='pics', blank=True, default="False")
    desc= models.TextField()
    price= models.IntegerField()

class ecmodel(models.Model):
    name= models.CharField(max_length=100)
    category =models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics', blank=True, default="False")
    img3 = models.ImageField(upload_to='pics', blank=True, default="False")
    img4 = models.ImageField(upload_to='pics', blank=True, default="False")
    img5 = models.ImageField(upload_to='pics', blank=True, default="False")
    desc= models.TextField()
    price= models.IntegerField()

class csmodel(models.Model):
    name= models.CharField(max_length=100)
    category =models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics', blank=True, default="False")
    img3 = models.ImageField(upload_to='pics', blank=True, default="False")
    img4 = models.ImageField(upload_to='pics', blank=True, default="False")
    img5 = models.ImageField(upload_to='pics', blank=True, default="False")
    desc= models.TextField()
    price= models.IntegerField()

class memodel(models.Model):
    name= models.CharField(max_length=100)
    category =models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics', blank=True, default="False")
    img3 = models.ImageField(upload_to='pics', blank=True, default="False")
    img4 = models.ImageField(upload_to='pics', blank=True, default="False")
    img5 = models.ImageField(upload_to='pics', blank=True, default="False")
    desc= models.TextField()
    price= models.IntegerField()

class eemodel(models.Model):
    name= models.CharField(max_length=100)
    category =models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics', blank=True, default="False")
    img3 = models.ImageField(upload_to='pics', blank=True, default="False")
    img4 = models.ImageField(upload_to='pics', blank=True, default="False")
    img5 = models.ImageField(upload_to='pics', blank=True, default="False")
    desc= models.TextField()
    price= models.IntegerField()

class tcmodel(models.Model):
    name= models.CharField(max_length=100)
    category =models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics', blank=True, default="False")
    img3 = models.ImageField(upload_to='pics', blank=True, default="False")
    img4 = models.ImageField(upload_to='pics', blank=True, default="False")
    img5 = models.ImageField(upload_to='pics', blank=True, default="False")
    desc= models.TextField()
    price= models.IntegerField()

class melmodel(models.Model):
    name= models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics', blank=True, default="False")
    img3 = models.ImageField(upload_to='pics', blank=True, default="False")
    img4 = models.ImageField(upload_to='pics', blank=True, default="False")
    img5 = models.ImageField(upload_to='pics', blank=True, default="False")
    desc= models.TextField()
    price= models.IntegerField()

class othermodel(models.Model):
    name= models.CharField(max_length=100)
    category =models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics', blank=True, default="False")
    img3 = models.ImageField(upload_to='pics', blank=True, default="False")
    img4 = models.ImageField(upload_to='pics', blank=True, default="False")
    img5 = models.ImageField(upload_to='pics', blank=True, default="False")
    desc= models.TextField()
    price= models.IntegerField()
    
class cartmodel(models.Model):
    username= models.CharField(max_length=100)
    productname= models.CharField(max_length=100)
    pcategory =models.CharField(max_length=100)
    price= models.IntegerField()
    desc= models.TextField()
    img= models.ImageField(upload_to='pics')
    uid= models.IntegerField()

class buyer(models.Model):
    username= models.CharField(max_length=100)
    uid = models.IntegerField()
    pname = models.CharField(max_length=100)
    pid = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    desc = models.TextField()
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.IntegerField()
    country = models.CharField(max_length=100)
    pcategory = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    
class reviewmodel(models.Model):
    department= models.CharField(max_length=100)
    pid= models.IntegerField()
    user= models.CharField(max_length=100)
    uid= models.IntegerField()
    title= models.TextField()
    review= models.TextField()
    star= models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True)