from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): 
# class Post is inherited models.Model
    Firstname = models.CharField(max_length=100)
    Lastname = models.TextField()
    date_of_birth = models.DateTimeField(default=timezone.now)



