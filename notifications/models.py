from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.shortcuts import reverse
from moonlit_farm.models import TimestampModel


class NotificationTypes(models.TextChoices):
    NEW_COW = 'new_cow'
    NEW_ACTIVITY = 'new_activity'
    NEW_PRODUCT = 'new_product'


class Notification(TimestampModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    is_seen = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    type = models.CharField(choices=NotificationTypes.choices, null=True, default=None, max_length=50)

    @property
    def message(self):
        if self.type == NotificationTypes.NEW_COW.value:
            return f'A new furry friend - {self.content_object.name} - has joined our farm.'
        elif self.type == NotificationTypes.NEW_ACTIVITY.value:
            return f'New activity available at the farm: {self.content_object.name}.'
        elif self.type == NotificationTypes.NEW_PRODUCT.value:
            return f'{self.content_object.name} has just been added to our list of products.'

        raise ValueError('Unhandled notification type')

    @property
    def link(self):
        if self.type == NotificationTypes.NEW_COW.value:
            return reverse('cows:details', args=(self.content_object.id, ))
        elif self.type == NotificationTypes.NEW_ACTIVITY.value:
            return reverse('activities:details', args=(self.content_object.id, ))
        elif self.type == NotificationTypes.NEW_PRODUCT.value:
            return reverse('products:details', args=(self.content_object.id, ))

        raise ValueError('Unhandled notification type')
