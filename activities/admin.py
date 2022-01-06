from django.contrib import admin
from activities.models import Activity
from notifications.utils import create_notification


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        create_notification(obj, 'new_activity')
