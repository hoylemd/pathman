from rest_framework import serializers
from charman.models import Character, Alignment, Language, Size

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
  owner = serializers.Field(source='owner.username')
  #alignment = serializers.Field(source='alignment.name')

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
        'armor_bonus', 'shield_bonus', 'natural_armor',
        'deflection_mod', 'ac_misc_mod',
        'fortitude_base_mod', 'fortitude_magic_mod', 'fortitude_misc_mod',
        'reflex_base_mod', 'reflex_magic_mod', 'reflex_misc_mod',
        'will_base_mod', 'will_magic_mod', 'will_misc_mod',
        'base_attack_bonus', 'spell_resistance',
        'languages',
        'update_date', 'owner')

class AlignmentSerializer(serializers.HyperlinkedModelSerializer):
  characters = serializers.HyperlinkedRelatedField(
      view_name='character-detail', many=True)

  class Meta:
    model = Alignment
    fields = ('url', 'name',)

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
  characters = serializers.HyperlinkedRelatedField(
      view_name='character-detail', many=True)

  class Meta:
    model = Language
    fields = ('url', 'name',)

class SizeSerializer(serializers.HyperlinkedModelSerializer):
  characters = serializers.HyperlinkedRelatedField(
      view_name='character-detail', many=True)
  #races = serializers.HyperlinkedRelatedField(
  #    view_name='race-detail', many=True)

  class Meta:
    model = Size
    fields = ('url', 'name', 'mod', 'special_mod', 'fly_mod', 'stealth_mod')

