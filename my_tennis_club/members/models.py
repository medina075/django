from django.db import models
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  city = models.CharField(max_length=200,null=True)
  genero = models.CharField(max_length=200,null=True)
  email = models.EmailField(null=True)
# Create your models here.
