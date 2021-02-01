from rest_framework import serializers
from django.contrib.auth.models import User
# Model Class imports
#from .models import UserProfile

'''
class SignupSerializer(serializers.ModelSerializer):
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
  
  class Meta:
    model = User
    fields = ['email','username', 'password', 'password2']
    extra_kwargs ={
      'password':{'write_only':True}
    }

  def save(self):
    signup = User(
      email = self.validated_data['email'],
      username = self.validated_data['username'],
    )
    password = self.validated_data['password']
    password2 = self.validated_data['password2']

    if password == password2:
      #check username
      if User.objects.filter(username=signup.username).exists():
        raise serializers.ValidationError({'username': 'A user with that username already exists.'})
      else:#check email
        if User.objects.filter(email=signup.email).exists():
          raise serializers.ValidationError({'email': 'A user with that email already exists'})
        else:
          #save signup data
          signup.set_password(password)
          signup.save()
          
          return signup
    else:
      raise serializers.ValidationError({'password': 'Both Passwords Must Be Matched!'})
    '''