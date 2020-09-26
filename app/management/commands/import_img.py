# import csv
# from django.core.management.base import BaseCommand
# from app.models import Product
#
#
# class Command(BaseCommand):
#     def add_arguments(self, parser):
#         pass
#
#     def handle(self, *args, **options):
#
#         with open('data.csv', 'r', encoding='utf-8') as csvfile:
#             data = csv.reader(csvfile, delimiter=';')
#             for el in data:
#                 Product.objects.create(name=)

# Phone.objects.create(id=line[0], name=line[1], image=line[2], price=line[3],
#                      release_date=line[4], lte_exists=line[5], slug=slugify(line[1]))
