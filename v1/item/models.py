from django.db import models
from django.conf import settings
from v1.shop.models import Shop, ShopBranch
from v1.user.models import User
from v1.category.models import Category

# Food Item model
class Item(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  price = models.FloatField()
  discount = models.FloatField(default=0)
  description = models.TextField()
  image = models.ImageField(upload_to='uploads/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  prepare_time = models.IntegerField(default = 0)
  created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE, blank=True, null=True)
  updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

  def discounted_price(self):
    return self.price - self.discount

  def __str__(self):
    return self.category.name + self.name + str(self.price)

# Order Cart model
class Cart(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='cart', on_delete=models.CASCADE)
  date_added = models.DateTimeField(auto_now_add=True)
  item = models.ManyToManyField(Item, related_name="cartItemsTest")

  def __str__(self):
    return self.user.username

# Order Cart Item model
class CartItem(models.Model):
  cart = models.ForeignKey(Cart, related_name="cartItems", on_delete=models.CASCADE)
  item = models.ForeignKey(Item, related_name="cartItems", on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural='Cart Items'

  def __str__(self):
    return self.item.name