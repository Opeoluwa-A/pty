from turtle import title
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
# Create your models here.

class Post(models.Model):
  Title = models.CharField(max_length=200) 
  Text = models.TextField()
  Author = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
  Created_date = models.DateTimeField()
  Published_date = models.DateTimeField()
  