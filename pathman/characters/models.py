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


class Character(InstrumentedModel):
    name = models.CharField(max_length=200)

    hp = models.IntegerField()

    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

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
