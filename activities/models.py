from django.db import models


class Activity(models.Model):
    class Meta:
        verbose_name = 'activity'
        verbose_name_plural = 'activities'
        ordering = ('-id',)

    name = models.CharField(max_length=128, unique=True, null=False)
    description = models.CharField(max_length=10000, default='')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Activity object ID = {self.id}>'
