from django.db import models
# import models from other apps
from v1.users.models import User
from v1.item.models import Item, CustomizationGroup, CustomizationItem, ModifierGroup

# Cart model
class Cart(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uuid

    class Meta:
        verbose_name_plural = 'Carts'

# Cart model
class CartItem(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    cart = models.ForeignKey(Cart, related_name="cartItems", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name="cartItems", on_delete=models.CASCADE)

    class Meta:
    verbose_name_plural='Cart Items'

    def __str__(self):
        return self.item.name