from django.db import models


class CryptoPurchased(models.Model):
    asset_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    quantity_purchased = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    amount_purchased = models.DecimalField(max_digits=19,decimal_places=10)
    amount_invested = models.DecimalField(max_digits=19,decimal_places=2)
    date_purchased = models.DateField()

    def __str__(self):
        return self.asset_id
    
class CryptoSold(models.Model):
    asset_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    quantity_sold = models.DecimalField(max_digits=19, decimal_places=2)
    amount_sold = models.DecimalField(max_digits=19, decimal_places=2)
    date_sold = models.DateField()

    def __str__(self):
        return self.asset_id




