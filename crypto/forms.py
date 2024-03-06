from django import forms
from .models import CryptoPurchased, CryptoSold

class CryptoPurchasedForm(forms.ModelForm):

    class Meta:
        model = CryptoPurchased
        fields = ('name','asset_id','amount_invested', 'amount_purchased','quantity_purchased','date_purchased')
        widgets = {
            'date_purchased': forms.DateInput(attrs={
                'type':'date',
            }),
        }

class CryptoSoldForm(forms.ModelForm):

    class Meta:
        model = CryptoSold
        fields = (
            'name',
            'asset_id',
            'amount_sold', 
            'quantity_sold', 
            'date_sold',
        )