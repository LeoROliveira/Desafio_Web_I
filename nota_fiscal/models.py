from django.db import models

# Create your models here.
class nota_fiscal(models.Model):
    Numero = models.CharField(max_length=100)
    Vendedor = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=100)
    Descrição = models.CharField(max_length=100)
    Valor = models.CharField(max_length=100)
def __str__(self):
    return self.numero