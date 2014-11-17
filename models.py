from django.db import models

def ability_score_to_modifier(score):
  return (score / 2) - 5;

# Create your models here.
class Character(models.Model):
  # character information
  name = models.CharField(max_length=200)
  race = models.CharField(max_length=200)
  character_class = models.CharField(max_length=200)
  level = models.IntegerField()

  # ability scores
  strength = models.IntegerField()
  dexterity = models.IntegerField()
  constitution = models.IntegerField()
  intelligence = models.IntegerField()
  wisdom = models.IntegerField()
  charisma = models.IntegerField()

  # ability modifiers
  @property
  def strength_modifier(self):
    return ability_score_to_modifier(self.strength)
  @property
  def dexterity_modifier(self):
    return ability_score_to_modifier(self.dexterity)
  @property
  def constitution_modifier(self):
    return ability_score_to_modifier(self.constitution)
  @property
  def intelligence_modifier(self):
    return ability_score_to_modifier(self.intelligence)
  @property
  def wisdom_modifier(self):
    return ability_score_to_modifier(self.wisdom)
  @property
  def charisma_modifier(self):
    return ability_score_to_modifier(self.charisma)

  # meta data
  create_date = models.DateTimeField('date created')
  update_date = models.DateTimeField('date updated')

  #stringifier
  def __str__(self):
    return self.name

  class Meta:
    ordering = ('create_date',)

