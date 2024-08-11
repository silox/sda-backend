from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Get all active users whose email domain is not gmail.com"

    def handle(self, *args, **options):
        for user in User.objects.filter(is_active=True).exclude(email='@gmail.com'):
            print(user.first_name, user.last_name)
