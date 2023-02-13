from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=20, blank=False)
    model = models.CharField(max_length=20, blank=False)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=100)

    def __str__(self):
        return f'{self.brand} {self.model} id {self.id}'
