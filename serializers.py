from rest_framework import serializers

from charman import models


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Character
        fields = ('url', 'name', 'race', 'classes', 'alignment', 'size',
                  'level',
                  'age', 'gender', 'height', 'weight', 'hair', 'eyes',
                  'strength', 'dexterity', 'constitution',
                  'intelligence', 'wisdom', 'charisma',
                  'hit_points',
                  'base_speed', 'armored_speed', 'climb_speed',
                  'swim_speed', 'fly_speed',
                  'misc_initiative_modifier',
                  'armor_bonus', 'shield_bonus', 'natural_armor',
                  'deflection_mod', 'ac_misc_mod',
                  'fortitude_base_mod', 'fortitude_magic_mod',
                  'fortitude_misc_mod',
                  'reflex_base_mod', 'reflex_magic_mod', 'reflex_misc_mod',
                  'will_base_mod', 'will_magic_mod', 'will_misc_mod',
                  'base_attack_bonus', 'spell_resistance',
                  'languages',
                  'update_date', 'owner')


class SizeSerializer(serializers.HyperlinkedModelSerializer):
    characters = serializers.HyperlinkedRelatedField(
        view_name='character-detail', many=True, read_only=True)

    class Meta:
        model = models.Size


class RaceSerializer(serializers.HyperlinkedModelSerializer):
    characters = serializers.HyperlinkedRelatedField(
        view_name='character-detail', many=True, read_only=True)

    class Meta:
        model = models.Race


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    '''classes = serializers.HyperlinkedRelatedField(
        view_name='characterclass-detail', many=True, read_only=True)
        '''

    class Meta:
        model = models.Skill


class CharacterClassSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.CharacterClass


class ClassLevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ClassLevel


class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Feature


class FeatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Feat
