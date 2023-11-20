from django.db import models

# Create your models here.

class Item(models.Model):#inherit the functions inside Models to use in the Item()
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    #a field can not be created it it is empty or without text.
    #it will be checked as not done by default.
    