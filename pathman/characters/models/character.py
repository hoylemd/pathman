from django.core.urlresolvers import reverse
from django.db import models

from .abstract import InstrumentedModel
from .character_class import CharacterClass


def ability_modifier(score):
    return score / 2 - 5


class Character(InstrumentedModel):
    hp = models.IntegerField()

    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    classes = models.ManyToManyField(CharacterClass, through='ClassLevel')

    @property
    def strength_mod(self):
        return ability_modifier(self.strength)

    @property
    def dexterity_mod(self):
        return ability_modifier(self.dexterity)

    @property
    def constitution_mod(self):
        return ability_modifier(self.constitution)

    @property
    def intelligence_mod(self):
        return ability_modifier(self.intelligence)

    @property
    def wisdom_mod(self):
        return ability_modifier(self.wisdom)

    @property
    def charisma_mod(self):
        return ability_modifier(self.charisma)

    @property
    def classes_and_levels(self):
        classes = self.classlevel_set.all()
        string = ', '.join(c_class.summary for c_class in classes)

        if string == '':
            string = "A classless peasant!"

        return string

    def get_absolute_url(self):
        return reverse('characters:detail', args=[str(self.id)])
