from django.db import models

# Create your models here.
class UserApplication(models.Model):
    email = models.EmailField(null=True)
    name = models.CharField(max_length=127, null=True)
    phone = models.CharField(max_length=20, null=True)