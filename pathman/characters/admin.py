from django.contrib import admin

from .models import Character, CharacterClass, ClassLevel

admin.site.register(Character)
admin.site.register(CharacterClass)
admin.site.register(ClassLevel)
