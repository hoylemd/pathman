from django.views.generic.edit import CreateView

from .models import Character


class CharacterCreateView(CreateView):
    model = Character
    fields = ['name', 'hp', 'race', 'strength', 'dexterity', 'constitution',
              'intelligence', 'wisdom', 'charisma']
