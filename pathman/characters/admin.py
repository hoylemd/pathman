from django.contrib import admin

from .models import Character, CharacterClass, ClassLevel, Race


class ClassLevelInline(admin.TabularInline):
    model = ClassLevel
    extra = 0


class CharacterAdmin(admin.ModelAdmin):
    inlines = (ClassLevelInline,)


admin.site.register(Character, CharacterAdmin)
admin.site.register(CharacterClass)
admin.site.register(Race)
