from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import pgettext_lazy


@python_2_unicode_compatible
class EuropeanVatRate(models.Model):
    country_code = models.CharField( max_length=2)
    data = JSONField()

    def __str__(self):
        return self.country_code
