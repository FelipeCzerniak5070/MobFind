from random import randint, choice
from faker import Faker

fake = Faker('pt_BR')

def rand_ratio():
    return randint(840, 900), randint(473, 573)

cities = [
    'Joaçaba',
    "Herval d'Oeste",
    'Luzerna',
    'Videira',
    'Capinzal',
]

property_titles = [
    'Apartamento Duplex',
    'Cobertura Duplex',
    'Casa com Piscina',
    'Casa Alto Padrão',
    'Apartamento Mobiliado',
    'Terreno Residencial',
]



def make_property():
    return {
        'id': fake.random_number(digits=5, fix_len=True),
        'title': choice(property_titles),
        'city': choice(cities),
        'price': randint(250000, 3500000),
        'bedrooms': randint(1, 5),
        'bathrooms': randint(1, 4),
        'garages': randint(0, 4),
        'area': randint(50, 450),
        'views': randint(50, 500),
        'featured': choice([True, False]),
        'image': {
            'url': 'https://loremflickr.com/%s/%s/architecture,house' % rand_ratio()
        }
    }


def make_properties(quantity=6):
    return [
        make_property()
        for _ in range(quantity)
    ]