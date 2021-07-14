from django.http import HttpResponse


def groups_allowed(groups=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.is_superuser:
                return view_func(request, *args, **kwargs)
            if not user.is_authenticated:
                return HttpResponse('You must be signed in!')

            if not user.groups.exists():
                return HttpResponse(f'You must be in one of the groups {", ".join(groups)}!')

            user_groups = [g.name for g in user.groups.all()]
            result = set(user_groups).intersection(groups)
            if groups and not result:
                return HttpResponse(f'You must be in one of the groups {", ".join(groups)}!')
            else:
                return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
