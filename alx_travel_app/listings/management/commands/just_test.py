"""Familiarizing my self with django manangement command."""
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = """Just Kiding."""
    def add_argument(self, parser):
        """A method that defined CLI arguments."""
        parser.add_argument('my_name', type=str)

    def handle(self, *args, **options):
        name = options['my_name']
        self.stdout.write(
            self.style.SUCCESS(f'Hello {name} nice to meet you!!')
        )