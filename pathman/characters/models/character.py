from django.core.urlresolvers import reverse
from django.db import models

from util.models import InstrumentedModel
from classes.models import Class
from races.models import Race


def ability_modifier(score):
    return score / 2 - 5


class Character(InstrumentedModel):
    hp = models.IntegerField()

    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)

    classes = models.ManyToManyField(Class, through='ClassLevel')

    race = models.ForeignKey(Race, null=True)

    def get_absolute_url(self):
        return reverse('characters:detail', args=[str(self.slug)])
