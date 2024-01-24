import datetime
from typing import Any
from django.core.management.base import BaseCommand
from hwapp.models import Thing
from random import choice,randint

class Command(BaseCommand):
    help = 'Create new things'

    def handle(self, *args: Any, **options: Any) -> str | None:
        things_names = ['Book', 'Pencile', 'Pen', 'Ruber', 'Highliter']
        for i in range(0,5):
            thing = Thing(
                thing_name = f'{things_names[i]}',
                description = f'Some description',
                price = randint(10, 100),
                quantity = randint(1, 100),
                thing_added_date = datetime.datetime.now(),
                )
            self.stdout.write(self.style.SUCCESS(f'Things {thing} created.'))
            thing.save()