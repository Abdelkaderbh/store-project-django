from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Fournisseur(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self):
        return self.name


class Categorie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Stock(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    status = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="stocks")
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE,related_name='stocks',null=True)

    def __str__(self):
        return self.product_name
