from django import forms
from .models import Expense, Category



class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('name', 'amount', 'date', 'category')
        widgets = {
            'name': forms.TextInput(attrs={"placeholder":"name", "class": "bg-white border text-black text-sm rounded-lg focus:ring-white focus:border-black block w-full p-2.5"}),
            'amount': forms.TextInput(attrs={"type":"number","min":"1","placeholder":"80$","class": "bg-white border border-black text-black text-sm rounded-lg focus:ring-white focus:border-black block w-full p-2.5"}),
            'date': forms.DateInput(attrs={"type":"date","class": "bg-white border border-black text-black text-sm rounded-lg focus:ring-white focus:border-black block w-full p-2.5"}),
            'category' : forms.Select(attrs={"class": "bg-white border border-black text-black text-sm rounded-lg focus:ring-white focus:border-black block w-full p-2.5"})
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'bg-white border border-black text-black text-sm rounded-lg focus:ring-white focus:border-black block w-full p-2.5'
                ,'id':'new_category'
            }),
        }
