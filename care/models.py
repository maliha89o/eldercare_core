from django.db import models

class CareService(models.Model):
    title = models.CharField(max_length=100)
    assigned_doctor = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title 