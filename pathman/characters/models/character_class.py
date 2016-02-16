from django.core.urlresolvers import reverse
from django.db import models, IntegrityError
from django.utils.text import slugify

from .abstract import InstrumentedModel


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
