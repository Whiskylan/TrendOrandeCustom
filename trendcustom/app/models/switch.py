from django.db import models

class Switch(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    TYPE_CHOICES = [
        ('linear', 'Linear'),
        ('tactile', 'Tactile'),
        ('click', 'Click'),
    ]
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
        )
    PIN_CHOICES = [
        ('5', '5'),
        ('3', '3'),
    ]
    pin = models.CharField(
        max_length=1,
        choices=PIN_CHOICES
        )
    image = models.ImageField(upload_to="app/switches/%Y/%m/%d", default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    url = models.URLField(default='')
    
    def __str__(self):
        return self.name