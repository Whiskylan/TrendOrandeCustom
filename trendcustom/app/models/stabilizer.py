from django.db import models

class Stabilizer(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="app/stabs/%Y/%m/%d", default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    url = models.URLField(default='')

    def __str__(self):
        return self.name