from django.contrib import admin

from .models import Character, ClassLevel


class ClassLevelInline(admin.TabularInline):
    model = ClassLevel
    extra = 0


class CharacterAdmin(admin.ModelAdmin):
    inlines = (ClassLevelInline,)


admin.site.register(Character, CharacterAdmin)
