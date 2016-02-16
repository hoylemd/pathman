from django.db import models

from model_utils.models import TimeStampedModel

from .character_class import CharacterClass
from .character import Character

class ClassLevel(TimeStampedModel):
    character_class = models.ForeignKey(CharacterClass,
                                        on_delete=models.CASCADE)
    character = models.ForeignKey(Character,
                                  on_delete=models.CASCADE)
    level = models.IntegerField(default=1)

    @property
    def summary(self):
        return "{} {}".format(self.character_class.name, self.level)

    def __str__(self):
        return "{}, {}".format(self.character.name, self.summary)
