from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Shop(models.Model):
  name = models.CharField(max_length=255)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='uploads/shop/', blank=True, null=True)
  is_verified = models.BooleanField(default= False)

  def __str__(self):
    return self.name

class Country(models.Model):
  name = models.CharField(max_length = 255)
  alpha_two_code = models.CharField(max_length = 2, blank=True, null=True)

  class Meta:
        verbose_name_plural = 'Countries'

  def __str__(self):
      return self.name

class BranchType(models.Model):
  name = models.CharField(max_length=16)

  def __str__(self):
    return self.name
  
class ShopBranch(models.Model):
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
  branch_type = models.ForeignKey(BranchType, on_delete=models.DO_NOTHING)
  location = models.CharField(max_length=255, blank=True, null=True)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=255, blank=True, null=True)
  country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
  description = models.TextField()
  opening_time = models.TimeField()
  closing_time = models.TimeField()

  class Meta:
        verbose_name_plural = 'Shop Branches'

  def __str__(self):
      return self.shop.name

# model to handle the relationship between a User and
# a particular branch for authorization
class UserBranch(models.Model):
  PermissionChoices = [
        (0, 'Viewer'),      # viewer is the employee of the shopBranch. can view, manage all the orders
        (1, 'Moderator'),   # has CRU permission for catogery, items and has ^ permission
        (2, 'Editor'),      # has CRUD permission for catogery, items and has ^ permission
        (3, 'Admin')        # can edit branch, assign permission to other users and has ^ permission
    ]
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  permission = models.IntegerField(choices=PermissionChoices, default=0)
  branch = models.ForeignKey(ShopBranch, on_delete=models.CASCADE)

  def __str__(self):
    return self.user.email + ": " + str(self.permission)

  class Meta:
    unique_together = ['user', 'branch']
    verbose_name_plural = 'User Branches'