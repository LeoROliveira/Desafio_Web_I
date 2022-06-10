from django.db import models

# Create your models here.
class produto(models.Model):
    Nome = models.CharField(max_length=100)
    Código = models.CharField(max_length=100)
    Peso = models.CharField(max_length=100)
    Valor = models.CharField(max_length=100)
    Marca = models.CharField(max_length=100)
def __str__(self):
    return self.nome