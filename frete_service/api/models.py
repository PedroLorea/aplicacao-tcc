from django.db import models

from api.constants import FRETES_ESTADOS, RESERVATORIOS_MATERIAIS, TIPOS_PRODUTOS
from api.base.base_model import BaseModel

class Localizacao(BaseModel):
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=100, blank=True, null=True)


class Frete(BaseModel):
    tipo_produto = models.CharField(max_length=50, choices=TIPOS_PRODUTOS)
    quantidade = models.IntegerField()
    localizacao_coleta = models.ForeignKey(Localizacao, on_delete=models.CASCADE, related_name="localizacao_coleta")
    localizacao_entrega = models.ForeignKey(Localizacao, on_delete=models.CASCADE, related_name="localizacao_entrega")
    data_coleta = models.DateTimeField()
    data_entrega = models.DateTimeField()


class Motorista(BaseModel):
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=100)


class Caminhao(BaseModel):
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano_fabricacao = models.DateField()
    peso = models.IntegerField()
    altura = models.FloatField()
    capacidade = models.FloatField()
    localizacao_atual = models.ForeignKey(Localizacao, on_delete=models.CASCADE, related_name="localizao_atual")
    material_reservatorio = models.CharField(max_length=100, choices=RESERVATORIOS_MATERIAIS)


class Viagem(BaseModel):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE, related_name="motorista_operacao_frete")
    caminhao = models.ForeignKey(Caminhao, on_delete=models.CASCADE, related_name="caminhao_operacao_frete")
    frete = models.ForeignKey(Frete, on_delete=models.CASCADE, related_name="frete_operacao_frete")
    estado = models.CharField(max_length=50, choices=FRETES_ESTADOS)
