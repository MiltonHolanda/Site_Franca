from django.db import models

from datetime import datetime

class Campanha(models.Model):
    ETAPAS = [
        ("Grupo I","Grupo I"),
        ("16-Avos", "16-Avos"),
        ("Oitavas", "Oitavas"),
        ("Quartas", "Quartas"),
        ("Semi Final", "Semi final"),
        ("Final", "Final")
    ]
    placar = models.CharField(max_length=5, null=False, blank=False)
    adversario = models.CharField(max_length=100, null=False, blank=False)
    etapa = models.CharField(max_length = 100, choices=ETAPAS, default='')
    data = models.DateTimeField(default=datetime.now, blank = False)

    def __str__(self):
        return self.adversario

class Titulos(models.Model):
    IMPORTANCIA = [
        ("evento ","evento"),
        ("evento grande", "evento grande"),
    ]
    conquista = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=400, null=False, blank=False)
    ano = models.CharField(max_length=400, null=False, blank=False)
    importancia = models.CharField(max_length = 100, choices=IMPORTANCIA, default='')

    def __str__(self):
        return self.conquista
    
class Participacao(models.Model):
    COLOCACAO = [
        ("Em andamento","Em andamento"),
        ("Fase de grupos","Fase de grupos"),
        ("Oitavas", "Oitavas"),
        ("Quartas","Quartas"),
        ("4º Lugar", "4º Lugar"),
        ("3º Lugar","3º Lugar"),
        ("Vice-campeã", "Vice-campeã"),
        ("🏆 Campeã", "🏆 Campeã"),
    ]
    colocacao = models.CharField(max_length = 100, choices=COLOCACAO, default='')
    descricao = models.CharField(max_length=400, null=False, blank=False)
    ano = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.ano
    
class Curiosidades(models.Model):
    numero = models.CharField(max_length = 100, null=False, blank=False)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=400, null=False, blank=False)
    
    def __str__(self):
        return self.titulo

class Elenco(models.Model):
    numero = models.CharField(max_length = 100, null=False, blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    posicao = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.nome
    