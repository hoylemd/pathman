from django.db import models


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
    languages = models.CharField(max_length=200)
    traits = models.CharField(required=False, max_length=2000)

    # stringifier
    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=200)
    ability = models.CharField(max_length=5, choices=[
        ('str', 'STR'),
        ('dex', 'DEX'),
        ('con', 'CON'),
        ('int', 'INT'),
        ('wis', 'WIS'),
        ('cha', 'CHA')
    ])
    trained_only = models.BooleanField(default=False)

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
    spell_type = models.CharField(max_length=10, required=False, choices=[
        ('arcanae', 'Arcane'),
        ('divine', 'Divine'),
    ])
    spell_progression = models.CharField(
        max_length=10,
        required=False,
        choices=[
            ('abundant', 'Abundant'),
            ('full', 'Full'),
            ('moderate', 'Moderate'),
            ('minor', 'Minor'),
        ]
    )

    # stringifier
    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    # stringifier
    def __str__(self):
        return self.name


class Feat(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    prerequisite = models.CharField(max_length=200)
    feat_types = models.CharField(max_length=200)

    # stringifier
    def __str__(self):
        return self.name


class Character(models.Model):
    # character information
    name = models.CharField(max_length=200)
    race = models.ForeignKey('Race', related_name='characters')
    alignment = models.CharField(max_length=200)
    classes = models.ManyToManyField('CharacterClass',
                                     through='ClassLevel',
                                     null=True,
                                     default=None)
    size = models.ForeignKey('Size', related_name='characters')
    level = models.IntegerField(default=1)

    # Cosmetics
    age = models.CharField(max_length=200, required=False)
    gender = models.CharField(max_length=200, required=False)
    height = models.CharField(max_length=200, required=False)
    weight = models.CharField(max_length=200, required=False)
    hair = models.CharField(max_length=200, required=False)
    eyes = models.CharField(max_length=200, required=False)

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
    languages = models.CharField(max_length=200, required=False)
    # Complicated. Will do later

    # meta data
    update_date = models.DateTimeField('last updated', auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='characters')

    # stringifier
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('update_date',)


class ClassLevel(models.Model):
    character = models.ForeignKey('Character')
    character_class = models.ForeignKey('CharacterClass')
    level = models.IntegerField()
    preferred = models.BooleanField(default=False)

    # meta data
    owner = models.ForeignKey('auth.User', related_name='classlevels')
