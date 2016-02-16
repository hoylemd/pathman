from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel


class InstrumentedModel(TimeStampedModel):
    slug = models.SlugField(unique=True)
    created_by = models.ForeignKey(User, null=True)

    class Meta:
        abstract = True


class CharacterClass(InstrumentedModel):
    name = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        slug_name = slugify(self.name)
        slug_number = 0

        if not self.slug:
            self.slug = slug_name
            slug_number += 1

        while True:
            try:
                return super(CharacterClass, self).save(*args, **kwargs)
            except IntegrityError:
                self.slug = slug_name + str(slug_number)
                slug_number += 1

    def get_absolute_url(self):
        return reverse('characters:class_detail', args=[str(self.id)])

    def __str__(self):
        return self.name


def ability_modifier(score):
    return score / 2 - 5


class Character(InstrumentedModel):
    name = models.CharField(max_length=200)

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

    def save(self, *args, **kwargs):
        slug_name = slugify(self.name)
        slug_number = 0

        if not self.slug:
            self.slug = slug_name
            slug_number += 1

        while True:
            try:
                return super(Character, self).save(*args, **kwargs)
            except IntegrityError:
                self.slug = slug_name + str(slug_number)
                slug_number += 1

    def get_absolute_url(self):
        return reverse('characters:detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class ClassLevel(TimeStampedModel):
    character_class = models.ForeignKey(CharacterClass,
                                        on_delete=models.CASCADE)
    character = models.ForeignKey(Character,
                                  on_delete=models.CASCADE)
    level = models.IntegerField()
