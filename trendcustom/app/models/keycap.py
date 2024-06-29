from django.db import models

class Keycap(models.Model):
    name = models.CharField(max_length=100)
    profile = models.ForeignKey('Keycap_Profile', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey('Keycap_Material', on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="app/keycaps/%Y/%m/%d", default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    url = models.URLField(default='')

    def __str__(self):
        return self.name