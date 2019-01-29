#from django.db import models

# Create your models here.

#items
from rest_framework import serializers

import uuid
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from users.models import MyUser


#class MyUser(AbstractUser):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#	 email = EmailField()
#    first_name = models.Charfield(max_length=10)
#    last_name = models.Charfield(max_length=10)   
#    location
#    mobile = models.Charfield(max_length=10)   
#    password_hashed = models.DateTimeField(default=models.CharField(max_length=10))
#	 date_registered = datetime.datetime.now()



#import uuid
#from django.db import models

class UserItem(models.Model):
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(MyUser, default=uuid.uuid4, editable=False)
    description = models.TextField()
    location = models.PointField(spatial_index=True, geography=True)
    date_posted = models.DateTimeField(default=datetime.datetime.now())
    cost = models.CharField(max_length=10) #giving away
    note = models.TextField()
    #for sale
#	for rent
#   sold
#.  rented  	
#   tags
#	pickup location

    class meta:
      db_table: "user_items"

#>>> eventobject = Event.objects.all()
#>>> eventobject.first().id
#'3cd2b4b0c36f43488a93b3bb72029f46'

#UserItem.objects.create(location=Point(lng, lat))
#from django.contrib.gis.geos import Point
#from django.contrib.gis.measure import D

#my_loc = Point(my_lng, my_lat)
#UserItem.objects.filter(location__distance_lte=(my_loc, D(m=5000))


#class UserItemTags(AbstractUser):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#	 tag = EmailField()
#book
#fitness
#health
#clothing
#luggage
#appliance


#class UserItem(models.model)
#	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#	item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class UserItemResponse(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_id = models.TextField()
    response_user_id = models.PointField(spatial_index=True, geography=True)
    message = models.DateTimeField(default=datetime.datetime.now())
    
#		tags
#		pickup location
