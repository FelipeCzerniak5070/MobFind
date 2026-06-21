from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/<str:user_type>/',
         views.login_view,
         name ='login'
         ),
    path(
        'property/<int:id>/',
        views.property_detail,
        name='property_detail',
    ),
    path('logout/',
         views.logout_view,
         name='logout'
    )
]
