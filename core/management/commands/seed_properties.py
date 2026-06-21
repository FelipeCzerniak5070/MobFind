from decimal import Decimal
from random import choice, randint

from django.core.management.base import BaseCommand

from core.models import (
    City,
    Property,
    PropertyType,
)


class Command(BaseCommand):
    help = 'Popula a tabela de imóveis'


    def handle(self, *args, **kwargs):

        Property.objects.all().delete()

        apartment = PropertyType.objects.get(
            name='Apartamento'
        )

        house = PropertyType.objects.get(
            name='Casa'
        )

        land = PropertyType.objects.get(
            name='Terreno'
        )

        cities = list(
            City.objects.all()
        )

        properties = [

            {
                'title': 'Apartamento Duplex Centro',
                'type': apartment,
                'price': Decimal('850000'),
                'area': 120,
                'bedrooms': 3,
                'bathrooms': 2,
                'garages': 2,
            },

            {
                'title': 'Casa Alto Padrão',
                'type': house,
                'price': Decimal('1450000'),
                'area': 280,
                'bedrooms': 4,
                'bathrooms': 3,
                'garages': 3,
            },

            {
                'title': 'Terreno Residencial',
                'type': land,
                'price': Decimal('280000'),
                'area': 450,
                'bedrooms': 0,
                'bathrooms': 0,
                'garages': 0,
            },

        ]

        for item in properties:

            Property.objects.create(
                title=item['title'],
                description=(
                    'Excelente oportunidade de investimento. '
                    'Imóvel localizado em região valorizada.'
                ),
                city=choice(cities),
                property_type=item['type'],
                price=item['price'],
                area=item['area'],
                bedrooms=item['bedrooms'],
                bathrooms=item['bathrooms'],
                garages=item['garages'],
                views=randint(20, 500),
                is_featured=True,
                is_active=True,
            )

        self.stdout.write(
            self.style.SUCCESS(
                'Imóveis cadastrados com sucesso.'
            )
        )