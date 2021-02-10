import uuid

from django.db import models
from django.conf import settings
from v1.shop.models import Shop, ShopBranch
from v1.user.models import User

# Food Category model
class Partner(models.Model): 
  STATUS_CHOICES = [
    (0, 'New'),
    (1, 'Documents Requested'),
    (2, 'Approved'),
    (3, 'Cancelled'),
    (4, 'Rejected'),
]

  uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  title = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField()
  phone = models.CharField(max_length=100)
  status = models.IntegerField(choices=STATUS_CHOICES, default=0)
  
      
  def __str__(self):
    return self.title 