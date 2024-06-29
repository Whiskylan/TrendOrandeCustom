from django.db import models

class Keycap_Profile(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name