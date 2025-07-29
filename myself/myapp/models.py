from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField()  
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name