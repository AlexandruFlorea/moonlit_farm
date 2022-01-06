from django.contrib import admin
from cows.models import Cow
from notifications.utils import create_notification


@admin.register(Cow)
class CowAdmin(admin.ModelAdmin):
    list_display = ['name', 'personality']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        create_notification(obj, 'new_cow')
