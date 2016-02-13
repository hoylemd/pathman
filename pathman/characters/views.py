from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Character


def index(request):
    return HttpResponse("Hello, world.")


class CharacterCreateView(CreateView):
    model = Character
    fields = ['name', 'hp']
