import uuid

from django.db import models
from v1.shop.models import Country


# Partner model
class Partner(models.Model):
    STATUS_CHOICES = [
        (0, 'New'),                # Application was just recieved
        (1, 'Pending'),            # Staffs have recieved the application
        (2, 'Waiting-Response'),   # We're waiting for the response from shop owners
        (3, 'Triaged'),            # The application is forwarded to shop and branch creation phase
        (4, 'Completed'),          # The shop, branch creation process is complete
        (5, 'Cancelled'),          # The application was cancelled by owner or is a spam
        (6, 'Rejected'),           # The application was rejected by the staff
    ]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)

    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
