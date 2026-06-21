from django.contrib import admin

from .models import (
    City,
    Property,
    PropertyType,
    Profile
)

admin.site.register(Profile)
admin.site.register(City)
admin.site.register(Property)
admin.site.register(PropertyType)
