from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    # Função responsavel por pela label do objeto numa lista
    def __str__(self):
        return self.nome
