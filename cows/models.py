from django.db import models


class Cow(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    personality = models.CharField(max_length=128, default='')
    description = models.CharField(max_length=10000, default='')

    def __str__(self):
        return self.name
