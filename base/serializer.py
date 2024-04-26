from rest_framework import serializers
from apex.models import Notepad
from django.contrib.auth.models import User


class Noteserializer(serializers.ModelSerializer):
    class Meta:
        model =Notepad
        fields = ['title' , 'note']

class Userserializer(serializers.ModelSerializer):
    password =serializers.CharField(write_only=True)
    class Meta:
        model =User
        fields =['username', 'email' ,'password']


class Loginserializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()