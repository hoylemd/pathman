from rest_framework import serializers
from charman.models import Character

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
  owner = serializers.Field(source='owner.username')

  class Meta:
    model = Character
    fields = ('url', 'name', 'race', 'classes', 'level',
        'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
        'update_date', 'owner')

