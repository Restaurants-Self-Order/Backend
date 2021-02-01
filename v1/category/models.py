import uuid

from django.db import models
from django.conf import settings
from v1.shop.models import Shop, ShopBranch
from v1.user.models import User

# Food Category model
class Category(models.Model):
  uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  branch = models.ForeignKey(ShopBranch, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  added_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
      
  def __str__(self):
    return self.name 