from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name
