from django.db import models

def ability_score_to_modifier(score):
  return (score / 2) - 5;

# Create your models here.
class Character(models.Model):
  # character information
  name = models.CharField(max_length=200)
  race = models.CharField(max_length=200)
  alignment = models.CharField(max_length=200, choices=[
      ('lawful_good', 'Lawful Good'),
      ('neutral_good', 'Neutral Good'),
      ('chaotic_good', 'Chaotic Good'),
      ('lawful_neutral', 'Lawful Neutral'),
      ('true_neutral', 'True Neutral'),
      ('chaotic_neutral', 'Chaotic Neutral'),
      ('lawful_evil', 'Lawful Evil'),
      ('neutral_evil', 'Neutral Evil'),
      ('chaotic_evil', 'Chaotic Evil')
    ])
  classes = models.CharField(max_length=200)
  size = models.CharField(max_length=200, default="medium", choices=[
      ('small', 'small'),
      ('medium', 'medium'),
      ('large', 'large'),
      ('huge', 'huge')
    ])
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
  # Complicated. Will do later

   # meta data
  update_date = models.DateTimeField('last updated', auto_now_add=True)
  owner = models.ForeignKey('auth.User', related_name='characters')

  # stringifier
  def __str__(self):
    return self.name

  class Meta:
    ordering = ('update_date',)

