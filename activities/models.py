from django.db import models


class Activity(models.Model):
    class Meta:
        verbose_name = 'activity'
        verbose_name_plural = 'activities'
        ordering = ('-id',)

    name = models.CharField(max_length=128, unique=True, null=False)
    quantity = models.IntegerField(default=0, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # max => 9999.99

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Activity object ID = {self.id}>'
