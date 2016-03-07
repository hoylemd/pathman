from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .models import Character


def ability_modifier(score):
    return score / 2 - 5


class CharacterCreateView(CreateView):
    model = Character
    fields = ['name', 'hp', 'race', 'strength', 'dexterity', 'constitution',
              'intelligence', 'wisdom', 'charisma']


class CharacterSheetView(DetailView):
    model = Character

    def get_context_data(self, **kwargs):
        return {
            'character': self.object,
            'strength_mod': ability_modifier(self.object.strength),
            'dexterity_mod': ability_modifier(self.object.dexterity),
            'constitution_mod': ability_modifier(self.object.constitution),
            'intelligence_mod': ability_modifier(self.object.intelligence),
            'wisdom_mod': ability_modifier(self.object.wisdom),
            'charisma_mod': ability_modifier(self.object.charisma)
        }
