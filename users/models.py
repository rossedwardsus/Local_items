#from django.db import models

# Create your models here.

#items
from rest_framework import serializers

import uuid
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models


class MyUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
#   password hashed
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)   
    #address
    #city
    #state
    date_registered = models.DateTimeField(default=datetime.datetime.now())
    

#import uuid
#from django.db import models

class UserItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    #location = models.PointField()
    date_posted = datetime.datetime.now()
    cost = models.CharField(max_length=10) #giving away
    note = models.TextField()
#		tags
#		pickup location

#>>> eventobject = Event.objects.all()
#>>> eventobject.first().id
#'3cd2b4b0c36f43488a93b3bb72029f46'



class UserSetting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    location = models.PointField()
    date_posted = datetime.datetime.now()
    cost = models.CharField(max_length=10) #giving away
    note = models.TextField()


#class UserItem(models.model)
#	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#	item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)