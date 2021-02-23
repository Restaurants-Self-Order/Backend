import uuid

from django.db import models
from v1.shop.models import ShopBranch
from v1.users.models import User
from v1.item.models import Item


# Food Category model
class Category(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    branch = models.ForeignKey(ShopBranch, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class ItemCategory(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name + self.category.name
