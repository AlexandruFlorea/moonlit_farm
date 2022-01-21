from django.db import models
from django.utils.text import slugify
from django.templatetags.static import static


class Activity(models.Model):
    class Meta:
        verbose_name = 'activity'
        verbose_name_plural = 'activities'
        ordering = ('-id',)

    name = models.CharField(max_length=128, unique=True, null=False)
    description = models.TextField(max_length=10000, default='')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Activity object ID = {self.id}>'

    @property
    def main_image(self):
        slug = slugify(self.name)

        return static(f'activities/images/{slug}.jpg')
