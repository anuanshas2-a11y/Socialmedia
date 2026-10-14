from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
   phone=models.CharField(max_length=100,unique=True)
   bio=models.CharField(max_length=100,blank=True)


class Post(models.Model):
   title=models.CharField(max_length=100,blank=True)
   image=models.ImageField(upload_to="post_images")
   caption=models.TextField(null=True)
   created_at=models.DateTimeField(auto_now_add=True)
   updated_at=models.DateTimeField(auto_now=True)
   owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="post")

   def __str__(self):
      return self.title
   

class Comment(models.Model):
   comment=models.CharField(max_length=100)
   owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="comment")
   post_obj=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comment")
   created_at=models.DateTimeField(auto_now_add=True)
   updated_at=models.DateTimeField(auto_now=True)


class Likes(models.Model):
   owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="likes")
   post_obj=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="likes")
   created_at=models.DateTimeField(auto_now_add=True)

   class Meta:
      unique_together=('owner','post_obj')