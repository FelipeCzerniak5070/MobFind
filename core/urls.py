from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'core'

urlpatterns = [
    path(
        'property/<int:id>/',
        views.property_detail,
        name='property_detail',
    ),
    path(
    'favorite/<int:id>/',
    views.toggle_favorite,
    name='toggle_favorite',
    ),
    path(
        'properties/',
        views.properties,
        name='properties'
    ),
    path('login/<str:user_type>/',
         views.login_view,
         name ='login'
         ),
    path('logout/',
         views.logout_view,
         name='logout'
    ),
    path('', views.home, name='home'),
    
]
