from django.contrib.auth.models import User, Group
from blogging.models import Post, Category
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        ordering = ['-id']
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Group
        fields = ['url', 'name']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Post
        fields = ['title', 'text', 'author', 'created_date',
                  'modified_date', 'published_date']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Category
        fields = ['name', 'description', 'posts']
