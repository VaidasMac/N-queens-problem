from django.db import models

# Create your models here.
class Post(models.Model):
    post = models.IntegerField(max_length=100)