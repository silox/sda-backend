from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Gets count of users with given first name"

    def add_arguments(self, parser):
        parser.add_argument("first_name", type=str)

    def handle(self, *args, **options):
        first_name = options["first_name"]
        user_count = User.objects.filter(first_name__iexact=first_name).count()
        print(f"User count with first_name={first_name}: {user_count}")
