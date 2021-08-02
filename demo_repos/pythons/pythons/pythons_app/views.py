from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Python

from ..core.mixins import GroupsAllowedMixin


class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'


class PythonCreateView(GroupsAllowedMixin, CreateView):
    template_name = 'create.html'
    model = Python
    fields = '__all__'
    success_url = reverse_lazy('sign in')


# def index(req):
#     pythons = Python.objects.all()
#     return render(req, 'index.html', {'pythons': pythons})


# @login_required(login_url=reverse_lazy('sign in'))
# @groups_allowed(groups=['User'])
# @groups_allowed(groups=['admin'])
# def create(request):
#     if request.method == 'GET':
#         form = PythonCreateForm()
#         return render(request, 'create.html', {'form': form})
#     else:
#         form = PythonCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#         return render(request, 'create.html', {'form': form})
