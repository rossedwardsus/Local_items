#from django.db import models

# Create your models here.

#items
from rest_framework import serializers

import uuid
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models


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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    location = models.PointField(spatial_index=True, geography=True)
    date_posted = models.DateTimeField(default=datetime.datetime.now())
    cost = models.CharField(max_length=10) #giving away
    note = models.TextField()
#		tags
#		pickup location

#>>> eventobject = Event.objects.all()
#>>> eventobject.first().id
#'3cd2b4b0c36f43488a93b3bb72029f46'


#class UserItemTags(AbstractUser):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#	 tag = EmailField()


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
