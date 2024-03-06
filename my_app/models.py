from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
 
class Income(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField(auto_now=True) 

    def __str__(self):
        return self.name
