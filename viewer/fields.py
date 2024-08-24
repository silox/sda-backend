from datetime import date

from django.core.exceptions import ValidationError
from django.forms import DateField


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class PastMonthField(DateField):
    def validate(self, value):
        super().validate(value)
        if value < date.today():
            raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)
