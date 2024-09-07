from django.contrib import admin

from accounts.filters import EmailDomainFilter
from accounts.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    @staticmethod
    def user_name(obj):
        return obj.user.username

    @staticmethod
    def user_email(obj):
        return obj.user.email

    @admin.action(description="Set Lorem Ipsum biography")
    def set_lorem_ipsum_bio(self, request, queryset):
        queryset.update(biography='Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

    ordering = ['id']
    list_display = ['id', 'user_name', 'user_email']
    list_display_links = ['id', 'user_name', 'user_email']
    list_per_page = 20
    list_filter = [EmailDomainFilter]
    search_fields = ['user__username', 'user__email']
    actions = ['set_lorem_ipsum_bio']


admin.site.register(Profile, ProfileAdmin)
