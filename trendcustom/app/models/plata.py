from django.db import models

class Plata(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    form_factor = models.ForeignKey('Form_Factor', on_delete=models.SET_NULL, null=True)
    PIN_CHOICES = [
        ('5', '5'),
        ('3', '3'),
    ]
    pin = models.CharField(
        max_length=1,
        choices=PIN_CHOICES
        )
    image = models.ImageField(upload_to="app/pcb/%Y/%m/%d", default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    url = models.URLField(default='')

    def __str__(self):
        return self.name
    
    @classmethod
    def get_form_factors(cls, selected_case_form_factor):
        return cls.objects.filter(form_factor=selected_case_form_factor)