from django.db import models

# Create your models here.
class Hours(models.Model):
    name = models.CharField(max_length=170)
    total_hours = models.DecimalField(max_digits=5, decimal_places=0)

    def total(self, name):
        return self.totalHours

    def __str__(self):
        return self.name


