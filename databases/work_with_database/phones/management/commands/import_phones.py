import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            Phone.objects.all().delete()

            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                record = Phone(id=int(line[0]),
                               name=line[1],
                               image=line[2],
                               price=int(line[3]),
                               release_date=datetime.strptime(line[4], "%Y-%m-%d"),
                               lte_exists=bool(line[5]),
                               slug=slugify(line[1]))
                record.save()
