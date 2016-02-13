from django.db import models
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel


class InstrumentedModel(TimeStampedModel):
    owner = models.ForeignKey(User)

    class Meta:
        abstract = True


class Character(InstrumentedModel):
    name = models.CharField(max_length=200)

    hp = models.IntegerField()

    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
