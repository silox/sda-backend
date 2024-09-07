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
