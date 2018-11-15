from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Spot(CommonModel):
    name = models.TextField(unique=True)
    details = models.TextField(blank=True)
    location = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'spot'
        verbose_name_plural = 'spots'
        indexes = [
            models.Index(fields=['name']),
        ]
    
    def __str__(self):
        return '{}'.format(self.name)


class Category(CommonModel):
    name = models.CharField(max_length=255, unique=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        indexes = [
            models.Index(fields=['name'])
        ]
    
    def __str__(self):
        return '{}'.format(self.name)


class Dish(CommonModel):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, )
    cost = models.DecimalField('cost', max_digits=11, decimal_places=2, blank=True, null=True)
    details = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'dish'
        verbose_name_plural = 'dishes'
        unique_together = (('spot', 'name'),)
        indexes = [
            models.Index(fields=('spot', 'name'))
        ]
    
    def __str__(self):
        return '{}'.format(self.name)


class DishModifier(CommonModel, MPTTModel):
    parent = TreeForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='extra')
    name = models.CharField(max_length=255)
    dish = models.ForeignKey(Dish, on_delete=models.DO_NOTHING, related_name='dish_modifiers')
    details = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'modifier'
        verbose_name_plural = 'modifiers'
    
    def __str__(self):
        return '{}'.format(self.name)
