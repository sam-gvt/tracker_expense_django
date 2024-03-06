from django.contrib import admin
from .models import CryptoPurchased, CryptoSold

admin.site.register(CryptoPurchased)
admin.site.register(CryptoSold)