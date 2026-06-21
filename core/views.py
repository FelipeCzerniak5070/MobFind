from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.contrib.auth.models import User
from .models import Profile, Property
from django.contrib.auth import logout

def home(request):
    context = {
        'properties': Property.objects.filter(is_active=True)
    }

    return render(
        request,
        'pages/home.html',
        context
    )
    
def property_detail(request, id):
    property = get_object_or_404(
        Property,
        pk=id
    )

    context = {
        'property': property,
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