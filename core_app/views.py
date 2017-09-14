from django.views.generic import ListView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from .models import User
# Create your views here.


class UserList(ListView):
    model = User
    queryset = User.objects.all().order_by('-created')


class UserList(ListView):
    model = User
    queryset = User.objects.all().order_by('-created')


class UserCreate(CreateView):
    model = User
    fields = ('name', 'email')
    success_url = reverse_lazy('user-list')