from django.db import models

from model_utils.models import TimeStampedModel

from classes.models import Class
from .character import Character


class ClassLevel(TimeStampedModel):
    the_class = models.ForeignKey(Class,
                                        on_delete=models.CASCADE)
    character = models.ForeignKey(Character,
                                  on_delete=models.CASCADE)
    level = models.IntegerField(default=1)

    @property
    def summary(self):
        return "{} {}".format(self.the_class.name, self.level)

    def __str__(self):
        return "{}, {}".format(self.character.name, self.summary)
