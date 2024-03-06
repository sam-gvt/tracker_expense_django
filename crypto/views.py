import json
from django.http import JsonResponse

from django.shortcuts import render, redirect
import requests
from .forms import CryptoPurchasedForm, CryptoSoldForm
from .models import CryptoPurchased, CryptoSold
from config import url, API_KEY
from django.views.decorators.csrf import csrf_exempt




def cryptos_sold(request):
    cryptos_sold = CryptoSold.objects.all()
    return render(request, 'crypto/index.html', {'cryptos_sold':cryptos_sold})


def add_crypto_purchased(request):

    if request.method == "POST":
        form = CryptoPurchasedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crypto')

    else:
        crypto_form = CryptoPurchasedForm()

    return render(request, 'crypto/add_crypto.html', {'crypto_form':crypto_form})

def add_crypto_sold(request):
    crypto_form = CryptoSoldForm()
    return render(request, 'crypto/add_crypto.html', {'crypto_form':crypto_form})


def crypto_purchased(request):
    my_cryptos = CryptoPurchased.objects.all

    return render(request, 'crypto/index.html', {'my_cryptos':my_cryptos})


@csrf_exempt
def get_api_data(request):
    headers = {
        'X-CoinAPI-Key': API_KEY,
    }
    my_bag = json.loads(request.body)

    all_assets = requests.get(url, headers=headers)
    all_assets = all_assets.json()

    _localStorage = []
    
    for data in all_assets:
        if data['asset_id'] in my_bag:
            new_value = { 
                'price_usd' : data['price_usd'],
                'asset_id' : data['asset_id']
            }
            _localStorage.append(dict(new_value))

    return JsonResponse(_localStorage, safe=False)

