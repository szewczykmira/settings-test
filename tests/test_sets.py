import django
django.setup()

from decimal import Decimal
import pytest

from django.core.exceptions import ImproperlyConfigured

from sets import utils
from sets.models import EuropeanVatRate


@pytest.fixture
def vat_country(db, json_success):
    data = json_success['rates']['AT']
    return EuropeanVatRate.objects.create(country_code='AT', data=data)


@pytest.mark.parametrize('rate_name,expected',
                         [('medicine', Decimal(20)), ('books', Decimal(10)),
                          (None, Decimal(20))])
def test_get_tax_for_country(vat_country, rate_name, expected):
    country_code = vat_country.country_code
    rate = utils.get_tax_for_country(country_code, rate_name)
    assert rate == expected


@pytest.mark.django_db
def test_get_tax_for_country_error():
    rate = utils.get_tax_for_country('XX', 'rate name')
    assert rate is None
