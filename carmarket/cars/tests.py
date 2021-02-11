import random

from django.test import TestCase
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'carmarket.settings'

from cars.management.commands.seed import gen_phone


class CarTestCase(TestCase):

    def test_all_pass(self):
        from cars.models import Make
        print(random.choice(list(Make)))
        pass



    def test_gen_phone(self):
        phone = gen_phone()
        print(phone)
