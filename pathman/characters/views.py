from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Character


def index(request):
    return HttpResponse("Hello, world.")


class CharacterCreateView(CreateView):
    model = Character
    fields = ['name', 'hp', 'strength', 'dexterity', 'constitution',
              'intelligence', 'wisdom', 'charisma']


class CharacterIndexView(ListView):
    model = Character


class CharacterDetailView(DetailView):
    model = Character
