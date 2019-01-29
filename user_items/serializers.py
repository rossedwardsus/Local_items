from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UserItem


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
        #encrypt password


#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = MyUser
#        fields = ('username', 'email')
         #encrypt password



#from django.contrib.auth.hashers import check_password, make_password
#password = "helloworld"
#h1 = make_password(password)
#check_password(password, h1)  # returns True
#check_password("incorrect", h1)  # returns False


class UserItemSerializer(serializers.Serializer):
    title = serializers.EmailField()
    date_posted = serializers.CharField(max_length=200)
    tags = serializers.DateTimeField()

    class Meta:
        model = UserItem
        fields = ('username', 'email')
    

    #def create(self, validated_data):
    #    return Comment(**validated_data)

    #def update(self, instance, validated_data):
    #    instance.email = validated_data.get('email', instance.email)
    #    instance.content = validated_data.get('content', instance.content)
    #    instance.created = validated_data.get('created', instance.created)
    #    return instance

