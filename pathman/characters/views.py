from django.views.generic.edit import CreateView

from .models import Character, CharacterClass


class CharacterCreateView(CreateView):
    model = Character
    fields = ['name', 'hp', 'strength', 'dexterity', 'constitution',
              'intelligence', 'wisdom', 'charisma']


class CharacterClassCreateView(CreateView):
    model = CharacterClass
    fields = ['name']
