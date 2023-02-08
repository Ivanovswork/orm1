import csv

from django.core.management.base import BaseCommand
# fropim phones.models import Phone
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('C:\\Users\\desti\\PycharmProjects\\pythonProject18\\work_with_database\\phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                ph = Phone(name=phone["name"],
                           image=phone["image"],
                           price=phone["price"],
                           release_date=phone["release_date"],
                           lte_exists=phone["lte_exists"],
                           slug=slugify(phone["name"])
                           )
                ph.save()
