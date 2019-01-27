from django.db import models

# Create your models here.

#items
from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance






#import uuid
#from django.db import models

#class Event(models.Model):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#    details = models.TextField()
#    years_ago = models.PositiveIntegerField()

#>>> eventobject = Event.objects.all()
#>>> eventobject.first().id
#'3cd2b4b0c36f43488a93b3bb72029f46'