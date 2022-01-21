from django.db import models
from django.utils.text import slugify
from django.templatetags.static import static


class Category(models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('-id',)

    name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Category ID=%s | name="%s"' % (self.id, self.name)


class Product(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    type = models.CharField(max_length=128, unique=False, null=False, default='physical')
    quantity = models.IntegerField(default=0, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)  # max => 999.99
    description = models.TextField(max_length=10000, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, default=None)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Product object ID = {self.id}>'

    @property
    def main_image(self):
        slug = slugify(self.name)

        return static(f'products/images/{slug}.jpg')
