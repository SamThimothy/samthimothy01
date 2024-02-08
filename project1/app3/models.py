from django.db import models

# Create your models here.

class Contact_Model(models.Model):
    name=models.CharField(max_length=120)
    mail=models.EmailField()
    choice=models.CharField(max_length=120)
    message=models.CharField(max_length=1000)