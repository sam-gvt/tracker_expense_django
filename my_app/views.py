from django.shortcuts import render
from .forms import ExpenseForm, CategoryForm
from .models import Expense
import datetime
from django.db.models import Sum

def index(request):
    expenses = Expense.objects.all()

    total_expenses = expenses.aggregate(Sum('amount'))

    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum('amount'))

    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum('amount'))

    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))

    categorical_sums = Expense.objects.filter().values('category__name').order_by('category__name').annotate(sum=Sum('amount'))
    return render(request, 'my_app/index.html', 
        {
            'expenses':expenses, 
            'total_expenses':total_expenses,
            'monthly_sum':monthly_sum,
            'weekly_sum':weekly_sum,
            'daily_sums':daily_sums,
            'categorical_sums':categorical_sums
        })


def add_expense(request):


    if request.method == "POST":
        if 'submit_add_category' in request.POST:
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()

        elif 'submit_add_expense' in request.POST:
            form = ExpenseForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print('aiiiie')

  
    expense_form = ExpenseForm()
    category_form = CategoryForm()

    return render(request, 'my_app/add_expense.html', {'expense_form':expense_form, 'category_form':category_form})
