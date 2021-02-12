import uuid

from django.db import models

from v1.user.models import User
from v1.category.models import Category


# Food Item model
class Item(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prepare_time = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE, blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def discounted_price(self):
        return self.price - self.discount

    def __str__(self):
        return self.category.name + self.name + str(self.price)
