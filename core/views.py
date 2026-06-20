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