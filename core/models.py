from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=2
    )

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return f'{self.name}/{self.state}'


class PropertyType(models.Model):
    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Profile(models.Model):

    CLIENT = 'client'
    REALTOR = 'realtor'

    ROLE_CHOICES = [
        (CLIENT, 'Cliente'),
        (REALTOR, 'Imobiliária'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )


class Property(models.Model):

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()
    

    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        related_name='properties'
    )

    property_type = models.ForeignKey(
        PropertyType,
        on_delete=models.PROTECT,
        related_name='properties'
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    area = models.PositiveIntegerField()

    bedrooms = models.PositiveSmallIntegerField(
        default=0
    )

    bathrooms = models.PositiveSmallIntegerField(
        default=0
    )

    garages = models.PositiveSmallIntegerField(
        default=0
    )

    image = models.ImageField(
        upload_to='properties/',
        blank=True,
        null=True,
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    views = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.title
    
