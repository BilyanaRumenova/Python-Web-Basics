from django.shortcuts import render, redirect

from expence_tracker_2.common.budget import calculate_budget_left
from expence_tracker_2.expenses_app.forms import ExpenseForm, DeleteExpenseForm
from expence_tracker_2.expenses_app.models import Expense
from expence_tracker_2.profile_app.models import Profile
from expence_tracker_2.profile_app.views import create_profile


def home_page(request):
    if Profile.objects.exists():
        profile = Profile.objects.all()[0]
        expenses = Expense.objects.all()

        context = {
            'profile': profile,
            'expenses': expenses,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return create_profile(request)


def create_expense(request):
    if request.method == 'GET':
        form = ExpenseForm()
        context = {
            'form': form
        }
        return render(request, 'expense-create.html', context)
    else:
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {
            'form': form
        }
        return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        form = ExpenseForm(instance=expense)
        context = {
            'expense': expense,
            'form': form
        }
        return render(request, 'expense-edit.html', context)
    else:
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {
            'expense': expense,
            'form': form
        }
        return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteExpenseForm(instance=expense)
        context = {
            'expense': expense,
            'form': form
        }
        return render(request, 'expense-delete.html', context)
    else:
        expense.delete()
        return redirect('home page')
