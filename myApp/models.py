from django.db import models
from django.utils.text import slugify


# Create your models here.
class product(models.Model):
    
    image = models.FileField(upload_to="img/%y")
    product_id = models.CharField(max_length=200)
    
    def __str__(self):
        return self.product_id


class testimonie(models.Model):
    
    image = models.FileField(upload_to="img/%y")
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    testimony = models.CharField(max_length=200000)

    def __str__(self):
        return self.name

class contacts(models.Model):
    name = models.CharField(max_length=2000, null=False, blank=False)
    email = models.CharField(max_length=2000, null=False, blank=False)
    subject = models.CharField(max_length=2000, null=False, blank=False)
    body = models.CharField(max_length=200000, null=False, blank=False)
     
   
    def __str__(self):
        return self.name


