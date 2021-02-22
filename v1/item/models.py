import uuid

from django.db import models

from v1.users.models import User
from v1.category.models import Category


# Food Item model
class Item(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    currency = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prepare_time = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE, blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


# Customiztion_Group model
class CustomiztionGroup(models.Model):
    customiztionChoices = [
        ('OPTIONAL', 'Optional'),
        ('REQUIRED', 'Required')
    ]
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    customiztion_type = models.CharField(
        max_length=20,
        choices=customiztionChoices,
        null=True
    )

    def __str__(self):
        return self.name

# Customization_Items
class Customization_Items(models.Model):
    paymentChoices = [
        ('PAID', 'Paid'),
        ('FREE', 'Free')
    ]
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    customiztionGroup = models.ForeignKey(CustomiztionGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    customiztion_type = models.CharField(
        max_length=20,
        choices = paymentChoices,
        null=True
    )

    class Meta:
        verbose_name_plural = 'Customization_Items'

    def __str__(self):
        return self.name


    
    
