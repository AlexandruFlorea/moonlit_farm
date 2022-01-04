from django.contrib import admin
from cows.models import Cow


@admin.register(Cow)
class CowAdmin(admin.ModelAdmin):
    list_display = ['name', 'personality']
