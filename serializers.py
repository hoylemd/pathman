from rest_framework import serializers

from charman import models


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')

    class Meta:
        model = models.Character


class SizeSerializer(serializers.HyperlinkedModelSerializer):
    characters = serializers.HyperlinkedRelatedField(
        view_name='character-detail', many=True)
    races = serializers.HyperlinkedRelatedField(
        view_name='race-detail', many=True)

    class Meta:
        model = models.Size


class RaceSerializer(serializers.HyperlinkedModelSerializer):
    characters = serializers.HyperlinkedRelatedField(
        view_name='character-detail', many=True)

    class Meta:
        model = models.Race


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    classes = serializers.HyperlinkedRelatedField(
        view_name='characterclass-detail')

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
