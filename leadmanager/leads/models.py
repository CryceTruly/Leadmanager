from django.db import models

# Create your models here.
class Lead(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=255,unique=True)
    message=models.CharField(max_length=5000,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    