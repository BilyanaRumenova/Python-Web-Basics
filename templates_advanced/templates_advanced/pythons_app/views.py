from django.shortcuts import render, redirect

from .forms import PythonCreateForm
from .models import Python
from ..core.decorators import groups_allowed


def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


# @login_required(login_url=reverse_lazy('sign in'))
@groups_allowed(groups=['User'])
def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'create.html', {'form': form})
