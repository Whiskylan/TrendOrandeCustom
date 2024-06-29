from django.db import models

class Case(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    form_factor = models.ForeignKey('Form_Factor', on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey('Case_Material', on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="app/cases/%Y/%m/%d", default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    url = models.URLField(default='')

    def __str__(self):
        return self.name
    
    @classmethod
    def get_form_factors(cls):
        return cls.objects.values_list('form_factor', flat=True).distinct()