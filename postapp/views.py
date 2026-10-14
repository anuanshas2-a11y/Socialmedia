from django.shortcuts import render
from postapp.serializers import *
from postapp.models import *
from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from postapp.permissions import IsOwner
from rest_framework.exceptions import ValidationError
# Create your views here.

class SighUpView(CreateAPIView):
    serializer_class=UserSerializer


class PostCreateView(CreateAPIView,ListAPIView):
    serializer_class=PostSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    queryset=Post.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class PostDeleteView(DestroyAPIView):
    serializer_class=PostSerializer
    permission_classes=[IsOwner]
    authentication_classes=[TokenAuthentication]
    queryset=Post.objects.all()

class CommentCreateView(CreateAPIView,ListAPIView):
    serializer_class=CommentSerializer
    permission_classes=[IsOwner,IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    queryset=Comment.objects.all()

    def perform_create(self, serializer):
        post_id = self.request.data.get('post_id')

        if not post_id:
            raise ValidationError({"post_id": "Post ID is required."})

        try:
            post_obj = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise ValidationError({"post_id": "Post does not exist."})

        return serializer.save(owner=self.request.user,post_obj=post_obj)
        
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class CommentRetriveView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=CommentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Comment.objects.all()    

  

class LikeCreateView(CreateAPIView,ListAPIView):
    serializer_class=LikeSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    queryset=Likes.objects.all()

    def perform_create(self, serializer):
        post_id = self.request.data.get('post_id')

        try:
            post_obj = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise ValidationError({"post_id": "Invalid post ID."})

        return serializer.save(post_obj=post_obj,owner=self.request.user)

class LikeListView(ListAPIView):
    serializer_class=LikeSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    queryset=Likes.objects.all()

    
class LikeDeleteView(DestroyAPIView):
    serializer_class=LikeSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner,IsAuthenticated]
    queryset=Likes.objects.all()

    