from django.db import models
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField


class InstrumentedModel(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    created_by = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
