from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Location(models.Model):
    locations = (
        ('Nairobi', 'Nairobi'),
        ('Kiambu', 'Kiambu'),
        ('Eastlands', 'Eastlands'),
        ('Machakos', 'Machakos'),
        ('Nakuru', 'Nakuru'),
        ('London', 'London'),
        ('Paris', 'Paris'),
        ('Vienna', 'Vienna'),
        ('Sydney', 'Sydney'),
        ('Stockholm', 'Stockholm'),
        ('Tokyo', 'Tokyo'),
        ('Hongkong', 'Hongkong'),        
        ('Thika', 'Thika'),
        ('Dubai', 'Dubai'),
        ('New York', 'New York'),
        ('Los Angeles', 'Los Angeles'),
        ('Venice', 'Venice'),
        ('Cairo', 'Cairo'),
        ('Himalayas', 'Himalyas'),
        ('Antarctica', 'Antarctica'),        
        ('Arctic', 'Arctic'), 
        ('Fantasy', 'Fantasy'),  
        ('Sparta', 'Sparta'),
        ('Mombasa', 'Mombasa'),        
    )
    name = models.CharField(max_length=65, choices=locations)



    def save_loc(self):
        self.save()

    def delete_loc(self):
        self.delete()


    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Hood(models.Model):
    name = models.CharField(max_length=50)
    image = ImageField()
    occupants = models.CharField(max_length=50)
    location = models.ForeignKey(Location)
    created_on = models.DateTimeField(auto_now_add=True, null=True)




   