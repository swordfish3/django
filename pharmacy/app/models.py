from django.db import models


class ProductManager(models.Manager):
    def create_product(self, pid, name, barcode):
        product = self.create(pid=pid, name=name, barcode=barcode)
        return product


class Product(models.Model):

    pid = models.CharField(default='111111111', max_length=100)
    name = models.CharField(default='test', max_length=200)
    barcode = models.BigIntegerField()

    objects = ProductManager()

    def __str__(self):
        return self.pid


class Meta:
    verbose_name_plural = 'products'
