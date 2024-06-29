from django.db import models

class Plate(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    form_factor = models.ForeignKey('Form_Factor', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="app/plates/%Y/%m/%d", default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    url = models.URLField(default='')

    def __str__(self):
        return self.name
    
    @classmethod
    def get_form_factors(cls, selected_case_form_factor):
        return cls.objects.filter(form_factor=selected_case_form_factor)