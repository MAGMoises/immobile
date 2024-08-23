from django.db import models
from datetime import datetime


# Cadastro de Clientes
class Client(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return "{} - {}".format(self.nome, self.email)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-id']

# Opções de Imóveis
class TypeImmobile(models.TextChoices):
    APARTMENT = 'APARTAMENTO', 'APARTAMENTO'
    KITNET = 'KITNET', 'KITNET'
    HOUSE = 'CASA', 'CASA'

# Cadastro de Imóveis
class Immobile(models.Model):
    code = models.CharField(max_length=100, verbose_name=("Código"))
    tipo_item = models.CharField(max_length=100, choices=TypeImmobile.choices, verbose_name=("Tipo de Item"))
    address = models.TextField(verbose_name=("Endereço"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=("Preço"))
    is_locate = models.BooleanField(default=False, verbose_name="está locado")
    
    def __str__(self):
        return "{} - {} - {}".format(self.code, self.tipo_item, self.is_locate)

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'
        ordering = ['-id']

# Cadastrar imagens do Imóvel
class ImmobileImage(models.Model):
    image = models.ImageField('Images', upload_to='images')
    immobile = models.ForeignKey(Immobile, related_name='immobile_images', on_delete=models.CASCADE, verbose_name=("Imóvel"))

    def __str__(self):
        return "Imagem de {}".format(self.immobile)

# Registrar Locação
class RegistrarLocation(models.Model):
    immobile = models.ForeignKey(Immobile, on_delete=models.CASCADE, related_name='reg_location', null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dt_start = models.DateTimeField('Inicio')
    dt_end = models.DateTimeField('Fim')
    create_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return "{} - {}".format(self.client, self.immobile)

    class Meta:
        verbose_name = 'Registrar Locação'
        verbose_name_plural = 'Registrar Locações'
        ordering = ['-id']
