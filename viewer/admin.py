from django.contrib import admin

from viewer.filters import TitleLengthFilter, MovieDecadeFilter
from viewer.models import Genre, Movie


class MovieAdmin(admin.ModelAdmin):
    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description='')

    @admin.action(description="Write release date to description")
    def write_release_to_description(self, request, queryset):
        for movie in queryset:
            movie.description = f'{movie.description}{"\n\n" if movie.description else ""}Released year - {movie.released.year}'
            movie.save()

    ordering = ['id']
    list_display = ['id', 'title', 'genre', 'released_year']
    list_display_links = ['id', 'title']
    list_per_page = 20
    list_filter = ['genre', TitleLengthFilter, MovieDecadeFilter]
    search_fields = ['title', 'genre__name']
    actions = ['cleanup_description', 'write_release_to_description']

    fieldsets = [
        (None, {'fields': ['title', 'created']}),
        (
            'External Information',
            {
                'fields': ['genre', 'released'],
                'description': (
                    'These fields are going to be filled with data parsed '
                    'from external databases.'
                )
            }
        ),
        (
            'User Information',
            {
                'fields': ['rating', 'description'],
                'description': 'These fields are intended to be filled in by our users.'
            }
        )
    ]
    readonly_fields = ['created']


class GenreAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name', 'available_for_children']
    list_display_links = ['id', 'name']
    list_filter = ['available_for_children']
    search_fields = ['name']


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
