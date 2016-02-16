from django.db import models
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel


class InstrumentedModel(TimeStampedModel):
    slug = models.SlugField(unique=True)
    created_by = models.ForeignKey(User, null=True)

    class Meta:
        abstract = True
