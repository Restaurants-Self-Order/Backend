import uuid

from django.db import models
from v1.shop.models import Country, Cusine

# Partner Application model
class PartnerApplication(models.Model):

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
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    designation = models.CharField(max_length=255)

    detailed_address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    shop_name = models.CharField(max_length=255)
    number_of_branches = models.IntegerField()
    cusine = models.ForeignKey(Cusine, on_delete=models.CASCADE)

    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Partner model
class Partner(models.Model):
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    detailed_address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    shop_name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

