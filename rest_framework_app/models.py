from django.db import models

# Create your models here.

class Employee(models.Model):
    firstname  = models.CharField(max_length=200)
    lastname  = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=20, decimal_places=2)



    def __str__(self):
        return f"{self.firstname} {self.lastname}"