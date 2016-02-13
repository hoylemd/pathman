from django import models

class Character(models.model):
    name = models.CharField(max_length=200)
