from django.contrib import admin

from viewer.models import Genre, Movie


class MovieAdmin(admin.ModelAdmin):
    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description='')

    ordering = ['id']
    list_display = ['id', 'title', 'genre', 'released_year']
    list_display_links = ['id', 'title']
    list_per_page = 20
    list_filter = ['genre']
    search_fields = ['title', 'genre__name']
    actions = ['cleanup_description']

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


admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
