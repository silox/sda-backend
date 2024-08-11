from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Prints user based on email"

    def add_arguments(self, parser):
        parser.add_argument("user_email", type=str)

    def handle(self, *args, **options):
        email = options["user_email"]
        user = User.objects.filter(email=email).first()
        if user is None:
            print('User does not exist')
            return

        print(user.first_name, user.last_name)
