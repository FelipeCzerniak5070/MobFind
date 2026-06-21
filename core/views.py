from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.contrib.auth.models import User
from .models import (
    Profile,
    Property,
    City,
    PropertyType,
    Favorite
    )
from django.contrib.auth import logout

def home(request):

    properties = Property.objects.filter(
        is_active=True
    )

    favorites_ids = []

    if request.user.is_authenticated:

        favorites_ids = list(

            Favorite.objects.filter(
                user=request.user
            ).values_list(
                'property_id',
                flat=True
            )

        )

    context = {

        'properties': properties,

        'favorites_ids': favorites_ids,

        'cities': City.objects.all(),

        'property_types': PropertyType.objects.all(),

        'selected_city': '',
        'selected_property_type': '',
        'selected_min_price': '',
        'selected_max_price': '',
    }

    return render(
        request,
        'pages/home.html',
        context,
    )
    
def property_detail(request, id):
    property = get_object_or_404(
        Property,
        id=id
    )
    
    favorites_ids = []

    if request.user.is_authenticated:

        favorites_ids = list(

            Favorite.objects.filter(
                user=request.user
            ).values_list(
                'property_id',
                flat=True
            )

        )
    

    context = {
        'property': property,
        'favorites_ids': favorites_ids,
        
    }

    return render(
        request,
        'pages/property-detail.html',
        context,
    )

def login_view(request, user_type):

    login_types = {
        'client': {
            'title': 'Área do Cliente',
            'subtitle': 'Acesse sua conta para buscar imóveis',
            'card_description': (
                'Entre ou crie sua conta para encontrar seu imóvel ideal'
            ),
        },

        'realtor': {
            'title': 'Área da Imobiliária',
            'subtitle': 'Gerencie seus imóveis e atendimentos',
            'card_description': (
                'Entre ou crie sua conta para gerenciar seus imóveis'
            ),
        },
    }

    context = login_types.get(user_type)

    if context is None:
        raise Http404()

    action = request.GET.get(
        'action',
        'login',
    )

    context['action'] = action

    if request.method == 'POST':

        action = request.POST.get(
            'action',
            'login',
        )

        # =====================
        # CADASTRO
        # =====================

        if action == 'register':
        
            uname = request.POST.get('uname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get(
                'confirm_password'
            )

            if password != confirm_password:

                messages.error(
                    request,
                    'As senhas não coincidem.'
                )

            elif User.objects.filter(
                email=email
            ).exists():

                messages.error(
                    request,
                    'Já existe uma conta com este email.'
                )

            else:

                user = User.objects.create_user(
                    username=uname,
                    email=email,
                    password=password,
                )

                Profile.objects.create(
                    user=user,
                    role=user_type,
                )

                login(
                    request,
                    user,
                )

                return redirect(
                    'core:home'
                )

        # =====================
        # LOGIN
        # =====================

        else:

            email = request.POST.get('email')
            password = request.POST.get('password')

            user_obj = User.objects.filter(
                email=email
            ).first()

            user = None

            if user_obj:

                user = authenticate(
                    request,
                    username=user_obj.username,
                    password=password,
                )

            if user is None:

                messages.error(
                    request,
                    'Usuário ou senha inválidos.'
                )

            elif user.profile.role != user_type:

                messages.error(
                    request,
                    'Esta conta não possui acesso a esta área.'
                )

            else:

                login(
                    request,
                    user,
                )

                return redirect(
                    'core:home'
                )

    return render(
        request,
        'pages/login.html',
        context,
    )
   
def logout_view(request):
    logout(request)
    return redirect('core:home')

def properties(request):

    favorites_ids = []

    if request.user.is_authenticated:

        favorites_ids = list(

            Favorite.objects.filter(
                user=request.user
            ).values_list(
                'property_id',
                flat=True
            )

        )
    
    properties = Property.objects.filter(
        is_active=True
    )

    city_id = request.GET.get('city')
    property_type_id = request.GET.get('property_type')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if city_id:
        properties = properties.filter(
            city_id=city_id
        )

    if property_type_id:
        properties = properties.filter(
            property_type_id=property_type_id
        )

    if min_price:
        properties = properties.filter(
            price__gte=min_price
        )

    if max_price:
        properties = properties.filter(
            price__lte=max_price
        )

    context = {
        'properties': properties,
        'cities': City.objects.all(),
        'property_types': PropertyType.objects.all(),

        'selected_city': city_id,
        'selected_property_type': property_type_id,
        'selected_min_price': min_price,
        'selected_max_price': max_price,
        'favorites_ids': favorites_ids,
    }

    return render(
        request,
        'pages/properties.html',
        context,
    )
    
@login_required
def toggle_favorite(request, id):

    property = get_object_or_404(
        Property,
        id=id,
    )

    favorite = Favorite.objects.filter(
        user=request.user,
        property=property,
    )

    if favorite.exists():

        favorite.delete()

    else:

        Favorite.objects.create(
            user=request.user,
            property=property,
        )

    return redirect(
        request.META.get(
            'HTTP_REFERER',
            'core:home',
        )
    )