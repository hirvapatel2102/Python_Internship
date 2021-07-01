from django.db import models

# Create your models here.
class watch(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    main_image = models.ImageField(upload_to = 'photos/whatch/')

class contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()

class about_us(models.Model):
    about_pera = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()
    location = models.CharField(max_length=200)
