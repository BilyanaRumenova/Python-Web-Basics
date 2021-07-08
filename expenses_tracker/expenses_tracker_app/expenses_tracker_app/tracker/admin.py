from django.contrib import admin

from expenses_tracker_app.tracker.models import Expense, Profile

admin.site.register(Expense)
admin.site.register(Profile)
