from django.core.management import BaseCommand
from conditions.fixtures.conditions_load import apply_fixtures


class Command(BaseCommand):
    help = 'Run the necessary fixture updates for the profile service.'

    def handle(self, *args, **options):
        """
        load conditions into the system
        :param args:
        :param options:
        :return:
        """

        apply_fixtures()
