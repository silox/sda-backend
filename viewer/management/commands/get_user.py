from django.core.management.base import BaseCommand
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


# Task 1
# Napis command, ktory vypise vsetkych uzivatelov (first_name, last_name), ktorych emailova adresa
# ma domenu @gmail.com (HINT: pouzi email__endswith=)

# Task 2
# Napis command, ktory vypise pocet uzivatelov s krstnym menom zadanym ako parameter commandu

# Task 3
# Napis command, ktory vypise vsetkych superuserov, zoradenych abecedne podla priezviska (field is_superuser)

# Task 4
# Napis command, ktory vypise vsetkych aktivnych uzivatelov (field is_active), ktorych emailova domena nekonci na @gmail.com.
