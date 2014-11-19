from rest_framework import serializers
from charman.models import Character

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
  owner = serializers.Field(source='owner.username')

  class Meta:
    model = Character
    fields = ('url', 'name', 'race', 'classes', 'alignment', 'size', 'level',
        'age', 'gender', 'height', 'weight', 'hair', 'eyes',
        'strength', 'dexterity', 'constitution',
        'intelligence', 'wisdom', 'charisma',
        'hit_points',
        'base_speed', 'armored_speed', 'climb_speed',
        'swim_speed', 'fly_speed',
        'misc_initiative_modifier',
        'armor_bonus', 'shield_bonus', 'natural_armor', 'size_modifier',
        'deflection_modifier', 'misc_ac_modifier',
        'update_date', 'owner')

