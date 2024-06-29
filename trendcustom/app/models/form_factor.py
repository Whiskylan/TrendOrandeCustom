from django.db import models
from django.core.validators import MaxValueValidator

class Form_Factor(models.Model):
    name = models.CharField(max_length=100)
    number_of_keys = models.IntegerField(validators=[MaxValueValidator(112)])

    def __str__(self):
        return self.name