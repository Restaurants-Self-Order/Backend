import uuid

from django.db import models

from v1.users.models import User
from v1.shop.models import ShopBranch


# Currency model
class Currency(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Currencies'


# Food Item model
class Item(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    branch = models.ForeignKey(ShopBranch, on_delete=models.CASCADE)

    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    price = models.IntegerField()

    image = models.URLField(blank=True, null=True)
    prepare_time = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE, blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


# CustomizationGroup model
class CustomizationGroup(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    required = models.BooleanField(default=False)
    min_select = models.IntegerField(default=0)
    max_select = models.IntegerField(default=0)
    branch = models.ForeignKey(ShopBranch, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Customization_Items
class CustomizationItem(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customization_group = models.ForeignKey(CustomizationGroup, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    branch = models.ForeignKey(ShopBranch, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.name + self.price


# Many to many between Item and CustomizationGroup
class ModifierGroup(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customization_group = models.ForeignKey(CustomizationGroup, on_delete=models.CASCADE)
    branch = models.ForeignKey(ShopBranch, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.name + self.customization_group.name

    class Meta:
        unique_together = ['item', 'customization_group']
