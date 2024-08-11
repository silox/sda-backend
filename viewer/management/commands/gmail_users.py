from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Gets all gmail.com domain users"

    def handle(self, *args, **options):
        for user in User.objects.filter(email__endswith='@gmail.com'):
            print(user.first_name, user.last_name)
