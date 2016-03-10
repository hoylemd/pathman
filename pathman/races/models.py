from django.core.urlresolvers import reverse

from util.models import InstrumentedModel


class Race(InstrumentedModel):
    def get_absolute_url(self):
        return reverse('race:detail', args=[str(self.slug)])
