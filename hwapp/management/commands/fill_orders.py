import datetime
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from hwapp.models import Order, Customer, Thing
from random import choice,randint
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Create new orders'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("customer_id", type=int, help='User ID')
        parser.add_argument('thing_id', type=int, help='Id of thing')
    

    def handle(self, *args, **options) -> None:
        customer_id = options['customer_id']
        thing_id = options['thing_id']

        customer = Customer.objects.get(id=customer_id)
        thing = Thing.objects.get(id=thing_id)

        order = Order(
            customer = customer,
            thing = thing,
            # quantity = randint(0,5),
            # sum = thing.price * thing.quantity
            sum = thing.price * randint(1,5))
        order.save()
        self.stdout.write(self.style.SUCCESS(f'New orders have been added: {order}'))



    # def handle(self, *args, **kwargs):
    #     customer_id = kwargs.get('customer_id')
    #     thing_id: list = kwargs.get('thing_id')

    #     customer = Customer.objects.filter(pk=customer_id).first()

    #     order = Order(customer=customer)
    #     sum = 0
    #     for i in range(0, 3):
    #         thing = Thing.objects.filter(pk=thing_id[i]).first()
    #         sum += (thing.price)
    #         order.sum = sum
    #         order.save()
    #         order.thing.add(thing)