from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View

from .models import Character, CharacterClass


class CharacterDetailView(DetailView):
    model = Character


class CharacterSheetView(View):
    def get(self, request, *args, **kwargs):
        character = get_object_or_404(Character, id=int(kwargs['pk']))
        return HttpResponse(
            "this is a character sheet for {}".format(character.name))


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
