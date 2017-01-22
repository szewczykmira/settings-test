from decimal import Decimal
import requests

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist
from django.utils import six

from .models import EuropeanVatRate


def get_tax_for_country(country_code, rate_name=None):
    try:
        country_vat = EuropeanVatRate.objects.get(country_code=country_code)
        reduced_rates = country_vat.data['reduced_rates']
        standard_rate = country_vat.data['standard_rate']
    except (KeyError, ObjectDoesNotExist):
        return None

    rate = standard_rate
    if rate_name is not None and rate_name in six.iterkeys(reduced_rates):
        rate = reduced_rates[rate_name]
    return Decimal(rate)
