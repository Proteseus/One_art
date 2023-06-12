from imaplib import _Authenticator
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *

# Create your views here.

@unauthenticated_user
def registerUser(request):
    radio = LoginType()
    form = NewBuyerForm()

    if request.POST:
        radio = request.POST['user_type']
        print(radio)
        if radio == 'Buyer':
            form = NewBuyerForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name = 'buyer')
                user.groups.add(group)
                
                print('Buyer created')
                messages.success(request, 'Account created for ' + username)
                return redirect('signin')

        elif radio == 'Artist':
            form = NewArtistForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                
                group = Group.objects.get(name = 'artist')
                user.groups.add(group)

                print('Artist created')
                messages.success(request, 'Account created for ' + username)
                return redirect('signin')

    context = {'form':form, 'radio':radio}
    return render(request, 'signup.html', context)

@unauthenticated_user
def loginPage(request):
    print(request.user)
    context = {}  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print('pre-login')
        if user is not None:
            login(request, user)
            print('Login')
            user = auth.get_user(request)
            group = request.user.groups.values_list('name', flat=True).first()
            print (group)
            if group == 'buyer':
                return redirect('buyer_temp')
            else:
                return redirect('artist')
        else:
            messages.info(request, 'Username or Password incorrect')
            return render(request, 'signin.html', context)
    return render(request, 'signin.html', context)

def logoutUser(request):
    logout(request)
    return redirect('signin')

def home(request):
    art = Artwork.objects.all()
    context = {'art':art}
    return render(request, 'index.html', context)

def browse(request):
    art = Artwork.objects.all()
    context = {'art':art}
    return render(request, 'browse_art.html', context)

@login_required(login_url='signin')
@allowed_users(allowed_roles=['buyer', 'admin'])
def buyer(request):
    art = Artwork.objects.all()
    buyer = Buyer.objects.all()
    context = {'art': art, 'buyer': buyer}
    return render(request, 'arts_buyer.html', context)

@login_required(login_url='signin')
def art(request):
    art = Artwork.objects.all()
    buyer = Buyer.objects.all()
    context = {'art': art, 'buyer': buyer}
    user = auth.get_user(request)
    group = request.user.groups.values_list('name', flat=True).first()
    if group == 'artist':
        return render(request, 'arts.html', context)
    else:
        return render(request, 'arts_buyer.html', context)

@login_required(login_url='signin')
@allowed_users(allowed_roles=['artist', 'admin'])
def createListing(request):
    form = CreateListing()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = CreateListing(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('assets')
    context = {'form':form}
    return render(request, 'artist.html', context)

@login_required(login_url='signin')
@allowed_users(allowed_roles=['artist', 'buyer'])
def updateOrder(request, pk):
    art = Artwork.objects.get(id=pk)
    art_name = art.name
    print(art_name)
    form = OrderForm(instance=art)

    user = auth.get_user(request)
    group = request.user.groups.values_list('name', flat=True).first()
    
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = OrderForm(request.POST, instance=art, initial=model_to_dict(art))
        if group == 'artist':
            arts = UpdateListing(request.POST, instance=art)
            arts.save()
            return redirect('assets')
        else:
            if form.is_valid():
                form.save()
                form1 = OrderForm(request.POST)
                form1.save()
                return redirect('assets_buyer')
    context = {'form':form, 'art_name':art_name}
    if group == 'artist':
        return render(request, 'update_art.html', context)
    else:
        return render(request, 'buy_art.html', context)


@login_required(login_url='signin')
@allowed_users(allowed_roles=['artist', 'admin'])
def deleteArt(request, pk):
    order = Artwork.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('assets')

    context = {'item':order}
    return render(request, 'delete.html', context)


@login_required(login_url='signin')
@allowed_users(allowed_roles=['artist', 'admin'])
def listArt(request):
    user = auth.get_user(request)
    print(user)
    art = Artwork.objects.all().filter(artist=user)
    context = {'art': art}
    return render(request, 'list_pieces.html', context)


@login_required(login_url='signin')
@allowed_users(allowed_roles=['buyer', 'admin'])
def listArtBuyer(request):
    user = auth.get_user(request)
    print(user)
    art = Artwork.objects.all().filter(owner=user)
    context = {'art': art}
    return render(request, 'arts_buyer.html', context)

    