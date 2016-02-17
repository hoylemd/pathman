from django.core.urlresolvers import reverse

from .abstract import InstrumentedModel


class CharacterClass(InstrumentedModel):
    def get_absolute_url(self):
        return reverse('characters:class_detail', args=[str(self.id)])
