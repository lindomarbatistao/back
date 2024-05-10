from django.db import models
import uuid

def upload_image(instance, filename):
    return f"{instance(str(uuid.uuid4()))}-{filename}"

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)


class Ponto(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
