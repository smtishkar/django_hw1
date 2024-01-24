from django.core.management.base import BaseCommand, CommandParser
from hwapp.models import Customer


class Command(BaseCommand):
    help = 'Delete customer'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('customer_id', type=int, help='client id')

    def handle(self, *args, **options):
        customer_id = options['customer_id']

        customer = Customer.objects.filter(pk=customer_id).first()

        self.stdout.write(self.style.ERROR(f'Customer {customer} deleted'))
        customer.delete()