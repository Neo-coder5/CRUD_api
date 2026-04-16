from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Book

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"