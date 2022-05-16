from sqlite3 import Timestamp
from pyexpat import model
from turtle import title
from django.db import models
from .helpers import *


# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    siteurl = models.CharField(max_length=255)
    shortdis = models.CharField(max_length=1000)
    email = models.EmailField()
    Timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    

    def __str__(self):
        return 'message from -' + self.siteurl + ' - ' + self.email 
   

class Games(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    siteurl = models.CharField(max_length=255)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)
    image = models.ImageField(upload_to='gameimage')

    def __str__(self):
        return self.title

    def save(self , *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Games, self).save(*args, **kwargs)

    