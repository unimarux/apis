from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    first_name = models.CharField(max_length=20 , verbose_name="First Name" , null=True , blank=True)
    last_name = models.CharField(max_length=20 , verbose_name="Last Name" , null=True , blank=True)
    email = models.EmailField(max_length=100 , verbose_name="Email" , null=True , blank=True)
    phone = models.CharField(max_length=13 , verbose_name="Phone Number" , unique=True ,
                             error_messages={"unique":"This phone number is already registered"})

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions',
        blank=True
    )


    def __str__(self):
        return self.username

class FoodType(models.Model):
    name = models.CharField(max_length=100 , unique=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    food_type = models.ForeignKey(FoodType , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField
    price = models.DecimalField(max_digits=10 , decimal_places=2)

    def __str__(self):
        return self.name


class Comment(models.Model):
    food = models.ForeignKey(Food , on_delete=models.CASCADE)
    username = models.ForeignKey(MyUser , on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment