from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20, default='')
    def __str__(self):
        return f'{self.category_name}'

class Item(models.Model):
    item_name = models.CharField(max_length=100, default='')
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.item_name}'

