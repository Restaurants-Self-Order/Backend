import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.dispatch import receiver
from v1.third_party.django.contrib.auth.managers import CustomUserManager

class Country(models.Model):
  uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  name = models.CharField(max_length = 50)
  alpha_two_code = models.CharField(max_length = 2)

  def __str__(self):
      return self.name
  
# custom User model with addditional fields of country, gender, phone and UserType
# changed the username field to email since we will use email for authentication 
# and registration
class UserType(models.Model):
  uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  name = models.CharField(max_length=16)

  def __str__(self):
      return self.name

class User(AbstractUser):
  uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
  GenderChoices = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Don\'t Specify'),
  ]
  email = models.EmailField(verbose_name='email', unique=True, max_length=255)
  phone = models.CharField(null=True, max_length=50)
  country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, null=True)
  user_type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING, blank=True, null=True)
  gender = models.CharField(
        max_length=1,
        choices=GenderChoices,
        null=True
    )
  REQUIRED_FIELDS = []
  USERNAME_FIELD = 'email'

  objects = CustomUserManager()

  def get_username(self):
    return self.email
    
# generate a random username and check if its already taken. 
# If taken, generate a username again until we find a valid username
def generate_username(instance):
  val = uuid.uuid4().hex[:30]
  x=0
  while True:
      if x == 0 and User.objects.filter(username=val).count() == 0:
        return val
      else:
        new_val = uuid.uuid4().hex[:30]
        if User.objects.filter(username=new_val).count() == 0:
          return new_val
      x += 1
      if x > 1000000:
        raise Exception("Name is super popular!")

def pre_save_post_receiver(sender, instance, *args,**kwargs):
  if not instance.username:
    instance.username= generate_username(instance)

#save the username before the User model is saved with the unique username
models.signals.pre_save.connect(pre_save_post_receiver, sender=User)

