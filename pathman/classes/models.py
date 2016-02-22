from django.core.urlresolvers import reverse

from util.models import InstrumentedModel


class Class(InstrumentedModel):
    def get_absolute_url(self):
        return reverse('class:detail', args=[str(self.slug)])
