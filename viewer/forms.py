import re

from django.forms import (
    CharField, IntegerField, ModelForm
)

from viewer.fields import PastMonthField, capitalized_validator
from viewer.models import Genre, Movie
from django.core.exceptions import ValidationError


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    title = CharField(validators=[capitalized_validator])
    rating = IntegerField(min_value=1, max_value=10)
    released = PastMonthField()

    def clean_description(self):
        # Každá věta bude začínat velkým písmenem
        initial = self.cleaned_data['description']
        if not initial:
            return ''
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        cleaned = '. '.join(sentence.capitalize() for sentence in sentences)
        self.cleaned_data['description'] = cleaned

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'Comedy' and result['rating'] > 5:
            self.add_error('genre', '')
            self.add_error('rating', '')
            raise ValidationError(
                "Commedies aren't so good to be rated over 5."
            )
        return result


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
