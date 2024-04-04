import random
from django.xpg.management.base import BaseCommand
from core.views import ecmodel

category = [ 'Tesla', 'car','I am Bad boy']

def generate_view_category():
    index = random.randint(0,2)
    return category[index]



class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='The txt file that contains the ecmodel name')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
                name = row
                category_name = generate_view_category()
 


