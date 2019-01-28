from django.db import models

# Create your models here.

#items
from rest_framework import serializers

import uuid
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser



#class MyUser(AbstractUser):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#	 email = EmailField()
#.   password hashed
#	 date_registered = datetime.datetime.now()
#    first name
#.   location



#import uuid
#from django.db import models

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
#    location = models.PositiveIntegerField()
    date_posted = datetime.datetime.now()
    cost = models.FloatField()
    note = models.TextField()
#		tags
#		pickup location

#>>> eventobject = Event.objects.all()
#>>> eventobject.first().id
#'3cd2b4b0c36f43488a93b3bb72029f46'




#class UserItem(models.model)
#	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#	item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)