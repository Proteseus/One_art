from asyncio.windows_events import NULL
from email.policy import default
from xml.dom.pulldom import default_bufsize
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Buyer(User):
    phone = models.CharField(max_length=200, null=True)
    user_type = models.CharField(max_length=200, default='Buyer')
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Artist(User):
    phone = models.CharField(max_length=200, null=True)
    user_type = models.CharField(max_length=200, default='Artist')
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Artwork(models.Model):
    name = models.CharField(max_length=200, null=True)
    piece = models.ImageField(null=True, upload_to='static/img/')
    artist = models.ForeignKey(Artist, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(Buyer, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SellLog(models.Model):
    STATUS = (
        ('On Sale', 'On Sale'),
        ('Sold', 'Sold')
    )

    name = models.ForeignKey(Artwork, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(Buyer, null=True, on_delete=models.SET_NULL)
    price = models.FloatField(null=True)
    date_sold = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.name
