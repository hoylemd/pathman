from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Character, CharacterClass


def index(request):
    return HttpResponse("Hello, world.")


class CharacterDetailView(DetailView):
    model = Character


class CharacterIndexView(ListView):
    model = Character


class CharacterCreateView(CreateView):
    model = Character
    fields = ['name', 'hp', 'strength', 'dexterity', 'constitution',
              'intelligence', 'wisdom', 'charisma']


class CharacterClassDetailView(DetailView):
    model = CharacterClass


class CharacterClassIndexView(ListView):
    model = CharacterClass


class CharacterClassCreateView(CreateView):
    model = CharacterClass
    fields = ['name']
