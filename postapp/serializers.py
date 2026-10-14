from rest_framework import serializers
from postapp.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","username","first_name","last_name","email","password","phone","bio"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"
        read_only_fields=["id","owner","created_at","updated_at"]

class CommentSerializer(serializers.ModelSerializer):
    owner=serializers.StringRelatedField(read_only=True)
    post_obj=serializers.StringRelatedField(read_only=True)


    class Meta:
        model=Comment
        fields="__all__"
        read_only_fields=["id","owner","post_obj","created_at","updated_at"]

class LikeSerializer(serializers.ModelSerializer):
    owner=serializers.StringRelatedField(read_only=True)
    post_obj=serializers.StringRelatedField(read_only=True)


    class Meta:
        model=Likes
        fields="__all__"
        read_only_fields=["id","owner","post_obj","created_at"]

        