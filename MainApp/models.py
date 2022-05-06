from enum import auto
from django.db import models

# Create your models here.

class Pizza(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=200)
    class Meta:
            verbose_name_plural = 'toppings'
    def __str__(self):
        return self.topping_name

class Entry (models.Model):
    topic = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    class Meta:
            verbose_name_plural = 'entries'
    def __str__(self):
        return self.text
