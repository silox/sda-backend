from django.contrib.admin import SimpleListFilter
from django.db.models.functions.text import Length


class TitleLengthFilter(SimpleListFilter):
    title = 'title length'
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        return (
            ("gt", "Title length > 12"),
            ("lt", "Title length <= 12"),
        )

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset

        annotated = queryset.annotate(title_length=Length("title"))
        if self.value() == "gt":
            return annotated.filter(title_length__gt=12)
        elif self.value() == "lt":
            return annotated.filter(title_length__lte=12)


class MovieDecadeFilter(SimpleListFilter):
    title = 'decade'
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        return (
            (1950, "50s"),
            (1960, "60s"),
            (1970, "70s"),
            (1980, "80s"),
            (1990, "90s"),
            (2000, "2000s"),
            (2010, "2010s"),
            (2020, "2020s"),
        )

    def queryset(self, request, queryset):
        try:
            return queryset.filter(released__year__gte=self.value(), released__year__lt=int(self.value()) + 10)
        except (ValueError, TypeError):
            pass
