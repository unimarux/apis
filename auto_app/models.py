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
        related_name='hexashop_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='hexashop_user_permissions',
        blank=True
    )


    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)

    def __str__(self):
        return self.name

