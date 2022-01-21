from django.db import models
from django.utils.text import slugify
from django.templatetags.static import static


class Cow(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    personality = models.CharField(max_length=128, default='')
    description = models.TextField(max_length=10000, default='')

    def __str__(self):
        return self.name

    @property
    def main_image(self):
        slug = slugify(self.name)

        return static(f'cows/images/main/{slug}.jpg')
