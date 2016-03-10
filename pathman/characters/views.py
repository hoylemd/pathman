from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .models import Character


def ability_struct(score):
    return {
        'score': score,
        'mod': score / 2 - 5
    }


class CharacterCreateView(CreateView):
    model = Character
    fields = ['name', 'hp', 'race', 'strength', 'dexterity', 'constitution',
              'intelligence', 'wisdom', 'charisma']


class CharacterSheetView(DetailView):
    model = Character

    def get_context_data(self, **kwargs):
        character = self.object
        return {
            'name': character.name,
            'race': character.race,
            'classes': character.classlevel_set.all(),
            'hp': character.hp,
            'strength': ability_struct(character.strength),
            'dexterity': ability_struct(character.dexterity),
            'constitution': ability_struct(character.constitution),
            'intelligence': ability_struct(character.intelligence),
            'wisdom': ability_struct(character.wisdom),
            'charisma': ability_struct(character.charisma)
        }
