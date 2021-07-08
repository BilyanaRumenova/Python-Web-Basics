from django.shortcuts import render

from expenses_tracker_app.tracker.common.budget import calculate_budget_left
from expenses_tracker_app.tracker.models import Profile, Expense
from expenses_tracker_app.tracker.views.profiles import create_profile


def index(request):
    if Profile.objects.exists():
        profile = Profile.objects.all()[0]
        expenses = Expense.objects.all()

        profile.budget_left = calculate_budget_left(profile, expenses)

        context = {
            'profile': profile,
            'expenses': expenses,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return create_profile(request)