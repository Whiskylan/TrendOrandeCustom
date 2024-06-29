from django.db import models
from django.conf import settings

class Completed_Keyboard(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    case = models.ForeignKey('Case', on_delete=models.SET_NULL, null=True)
    plata = models.ForeignKey('Plata', on_delete=models.SET_NULL, null=True)
    plate = models.ForeignKey('Plate', on_delete=models.SET_NULL, null=True)
    stabilizer = models.ForeignKey('Stabilizer', on_delete=models.SET_NULL, null=True)
    switch = models.ForeignKey('Switch', on_delete=models.SET_NULL, null=True)
    keycap = models.ForeignKey('Keycap', on_delete=models.SET_NULL, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Вызываем родительский конструктор
        self.case_price = self.case.price if self.case else None
        self.case_url = self.case.url if self.case else None
        self.plata_price = self.plata.price if self.plata else None
        self.plata_url = self.plata.url if self.plata else None
        self.plate_price = self.plate.price if self.plate else None
        self.plate_url = self.plate.url if self.plate else None
        self.stabilizer_price = self.stabilizer.price if self.stabilizer else None
        self.stabilizer_url = self.stabilizer.url if self.stabilizer else None
        self.switch_price = self.switch.price if self.switch else None
        self.switch_url = self.switch.url if self.switch else None
        self.keycap_price = self.keycap.price if self.keycap else None
        self.keycap_url = self.keycap.url if self.keycap else None
        self.total_price = sum([getattr(self, f'{field}_price') for field in ('case', 'plata', 'plate', 'stabilizer', 'switch', 'keycap') if getattr(self, f'{field}_price')])

    def __str__(self):
        return self.name