from nntplib import ArticleInfo
from pyexpat import model
from attr import field
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateListing(ModelForm):
    class Meta:
        model = Artwork
        fields = '__all__'

class UpdateListing(ModelForm):
    class Meta:
        model = Artwork
        fields = ["price"]


class OrderForm(ModelForm):
    class Meta:
        model = SellLog
        fields = '__all__'


class NewBuyerForm(UserCreationForm):
    class Meta:
        model = Buyer
        fields = ["username", "email", "phone", "password1", "password2"]


class NewArtistForm(UserCreationForm):
    class Meta:
        model = Artist
        fields = ["username", "email", "phone", "password1", "password2"]


CHOICES=(('Artist','I am an Artist'),
         ('Buyer','I am a Buyer'))


class LoginType(forms.Form):
    user_type = forms.ChoiceField(label='', choices=CHOICES, widget=forms.RadioSelect)
