from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Get all superusers ordered alphabetically by last name"

    def handle(self, *args, **options):
        for user in User.objects.filter(is_superuser=True).order_by('last_name'):
            print(user.first_name, user.last_name)
