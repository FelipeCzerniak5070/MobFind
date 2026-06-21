from django.http import Http404
from django.shortcuts import render
from utils import factory


def home(request):
    context = {
        'properties': factory.make_properties(6)
    }

    return render(
        request,
        'pages/home.html',
        context
    )
    
def property_detail(request, id):
    property = factory.make_property()

    context = {
        'property': property,
    }

    return render(
        request,
        'pages/property-detail.html',
        context,
    )
    
def login(request, user_type):

    login_types = {
        'client': {
            'title': 'Área do Cliente',
            'subtitle': 'Acesse sua conta para buscar imóveis',
            'card_title': 'Área do Cliente',
            'card_description': (
                'Entre ou crie sua conta para encontrar seu imóvel ideal'
            ),
        },

        'realtor': {
            'title': 'Área da Imobiliária',
            'subtitle': 'Gerencie seus imóveis e atendimentos',
            'card_title': 'Área da Imobiliária',
            'card_description': (
                'Entre ou crie sua conta para gerenciar seus imóveis'
            ),
        },
    }

    context = login_types.get(user_type)

    if not context:
        raise Http404()

    return render(
        request,
        'pages/login.html',
        context,
    )
    
