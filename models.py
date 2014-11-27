from django.db import models

def ability_score_to_modifier(score):
  return (score / 2) - 5;

# Create your models here.
class Character(models.Model):
  # character information
  name = models.CharField(max_length=200)
  race = models.ForeignKey('Race')
  alignment = models.ForeignKey('Alignment')
  classes = models.CharField(max_length=200)
  size = models.ForeignKey('Size')
  level = models.IntegerField(default=1)

  # Cosmetics
  age = models.CharField(max_length=200, null=True)
  gender = models.CharField(max_length=200, null=True)
  height = models.CharField(max_length=200, null=True)
  weight = models.CharField(max_length=200, null=True)
  hair = models.CharField(max_length=200, null=True)
  eyes = models.CharField(max_length=200, null=True)

  # Ability scores
  strength = models.IntegerField()
  dexterity = models.IntegerField()
  constitution = models.IntegerField()
  intelligence = models.IntegerField()
  wisdom = models.IntegerField()
  charisma = models.IntegerField()

  # Hp
  hit_points = models.IntegerField()

  # Speed
  base_speed = models.IntegerField()
  armored_speed = models.IntegerField(null=True)
  climb_speed = models.IntegerField(null=True)
  swim_speed = models.IntegerField(null=True)
  fly_speed = models.IntegerField(null=True)

  # Initiative
  misc_initiative_modifier = models.IntegerField(null=True)

  # Armor Class
  armor_bonus = models.IntegerField(null=True)
  shield_bonus = models.IntegerField(null=True)
  natural_armor = models.IntegerField(null=True)
  deflection_mod = models.IntegerField(null=True)
  ac_misc_mod = models.IntegerField(null=True)

  # Saves
  fortitude_base_mod = models.IntegerField()
  fortitude_magic_mod = models.IntegerField(null=True)
  fortitude_misc_mod = models.IntegerField(null=True)
  reflex_base_mod = models.IntegerField()
  reflex_magic_mod = models.IntegerField(null=True)
  reflex_misc_mod = models.IntegerField(null=True)
  will_base_mod = models.IntegerField()
  will_magic_mod = models.IntegerField(null=True)
  will_misc_mod = models.IntegerField(null=True)

  # Combat stats
  base_attack_bonus = models.IntegerField()
  spell_resistance = models.IntegerField(null=True)

  # Skills
  languages = models.ManyToManyField('Language')
  # Complicated. Will do later

   # meta data
  update_date = models.DateTimeField('last updated', auto_now_add=True)
  owner = models.ForeignKey('auth.User', related_name='characters')

  # stringifier
  def __str__(self):
    return self.name

  class Meta:
    ordering = ('update_date',)

class Alignment(models.Model):
  name = models.CharField(max_length=200)

  # stringifier
  def __str__(self):
    return self.name

  #('lawful_good', 'Lawful Good'),
  #    ('neutral_good', 'Neutral Good'),
  #    ('chaotic_good', 'Chaotic Good'),
  #    ('lawful_neutral', 'Lawful Neutral'),
  #    ('true_neutral', 'True Neutral'),
  #    ('chaotic_neutral', 'Chaotic Neutral'),
  #    ('lawful_evil', 'Lawful Evil'),
  #    ('neutral_evil', 'Neutral Evil'),
  #    ('chaotic_evil', 'Chaotic Evil')

class Language(models.Model):
  name = models.CharField(max_length=200)

  # stringifier
  def __str__(self):
    return self.name

class Size(models.Model):
  name = models.CharField(max_length=200)
  mod = models.IntegerField()
  special_mod = models.IntegerField()
  fly_mod = models.IntegerField()
  stealth_mod = models.IntegerField()

  # stringifier
  def __str__(self):
    return self.name

class Race(models.Model):
  name = models.CharField(max_length=200)
  ability_score_adj = models.CharField(max_length=200)
  size = models.ForeignKey('Size', default=5)
  base_speed = models.IntegerField()
  languages = models.ManyToManyField('Language')
  traits = models.CharField(max_length=1000, null=True)

  # stringifier
  def __str__(self):
    return self.name

class Skill(models.Model):
  name = models.CharField(max_length=200),
  ability = models.CharField(max_length=5, choices=[
    ('str', 'STR'),
    ('dex', 'DEX'),
    ('con', 'CON'),
    ('int', 'INT'),
    ('wis', 'WIS'),
    ('cha', 'CHA')
  ])
  trained_only = models.BooleanField(default=False)
  synergies = models.ManyToManyField('Skill')

  # stringifier
  def __str__(self):
    return self.name


class CharacterClass(models.Model):
  name = models.CharField(max_length=200)
  alignment = models.CharField(max_length=200)
  hit_die = models.IntegerField()
  starting_wealth = models.CharField(max_length=200)
  class_skills = models.ManyToManyField('Skill')
  skill_ranks = models.IntegerField()
  bab_progression = models.CharField(max_length=10, choices=[
    ('fast', 'Fast'),
    ('medium', 'Medium'),
    ('slow', 'Slow')
  ])
  fort_progression = models.CharField(max_length=5, choices=[
    ('good', 'Good'),
    ('bad', 'Bad')
  ])
  ref_progression = models.CharField(max_length=5, choices=[
    ('good', 'Good'),
    ('bad', 'Bad')
  ])
  will_progression = models.CharField(max_length=5, choices=[
    ('good', 'Good'),
    ('bad', 'Bad')
  ])
  spell_type = models.CharField(max_length=10, null=True, choices=[
    ('arcane', 'Arcane'),
    ('divine', 'Divine'),
    ('psionic', 'Psionic'),
    (None, 'None')
  ])
  spell_progression = models.CharField(max_length=10, null=True, choices=[
    ('full', 'Full'),
    ('moderate', 'Moderate'),
    ('minor', 'Minor'),
    (None, 'None')
  ])

  # stringifier
  def __str__(self):
    return self.name







