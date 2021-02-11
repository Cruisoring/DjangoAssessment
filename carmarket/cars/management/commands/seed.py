import random

from django.core.handlers.base import logger
from django.core.management import BaseCommand
from django_seed import Seed
from faker import Faker

from cars.models import Car, Make, Model, Years, Condition

# python manage.py seed --mode=refresh --number=100

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete Cars instances")
    Car.objects.all().delete()


def gen_phone():
    return f'0{str(random.randint(1, 9))} {str(random.randint(1, 9999)).zfill(4)} {str(random.randint(1, 9999)).zfill(4)}'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        self.run_seed()
        self.stdout.write('done.')

    def run_seed(self):
        """ Seed database based on mode

        :param mode: refresh / clear
        :return:
        """
        # Clear data from tables
        clear_data()

        seeder = Seed.seeder()
        fake = Faker()

        seeder.add_entity(Car, 100, {
            'SellerName': lambda x: fake.name(),
            'SellerMobile': lambda x: gen_phone(),
            'Make': lambda x: random.choice(list(Make)),
            'Model': lambda x: random.choice(list(Model)),
            'Year': lambda x: random.choice(list(Years))[0],
            'Condition': lambda x: random.choice(list(Condition)),
            'AskingPrice': lambda x: random.randint(100, 500) * 10,
        })
        inserted_pks = seeder.execute()

