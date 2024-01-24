import datetime
from typing import Any
from django.core.management.base import BaseCommand
from hwapp.models import Customer
from random import choice,randint

class Command(BaseCommand):
    help = 'Create new customers'

    def handle(self, *args: Any, **options: Any) -> str | None:
        names = ['John', 'Jane', 'Jack', 'Ivan', 'Sergey']
        for i in range(1,11):
            customer = Customer(
                name = f'{choice(names)}',
                email = f'mail{i}@example.com',
                tel = f'{randint(1000000, 9999999)}',
                address = f'Somewhere in the world',
                created_at = datetime.datetime.now(),
                )
            self.stdout.write(self.style.SUCCESS(f'Customer {customer} created.'))
            customer.save()