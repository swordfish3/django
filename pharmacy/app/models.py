from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    barcode = models.CharField(max_length=100)
    name = models.CharField(max_length=512)
    retail = models.DecimalField(max_length=50, max_digits=5, decimal_places=2)
    wholesale = models.DecimalField(max_length=100, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'products'
