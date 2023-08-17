from django.db import models

# Create your models here.

class Uploader(models.Model):
    tittle = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to ='uploads/', max_length=250)