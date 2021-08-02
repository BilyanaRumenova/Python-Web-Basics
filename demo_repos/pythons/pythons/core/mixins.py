from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import redirect, render

class GroupsAllowedMixin:
    required_groups = []

    def dispatch(self, request, *args, **kwargs):
        user = request.user

        if user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        if not user.is_authenticated:
            raise PermissionDenied

        if not user.groups.exists():
            raise PermissionDenied

        user_groups_names = [g.name for g in user.groups.all()]
        result = set(user_groups_names).intersection(self.required_groups)
        if self.required_groups and not result:
            return PermissionDenied

        return super().dispatch(request, *args, **kwargs)

