# Django imports
from django.shortcuts import render
from django.http import JsonResponse
# DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
# Serializer Class imports
#from .serializers import SignupSerializer 
# Model Class imports
#from .models import UserProfile

# Website home page method
def home(request):
  return render(request, 'index.html')

# APIs for category and Item
@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'User registration':'/sign-up',
    'User Sign In':'/sign-in',
    }
  return Response(api_urls)
'''
@api_view(['POST'])
def signUp(request):
    if request.method == "POST":
        serializer = SignupSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            signup = serializer.save()
            #save signup data
            userprofile = Userprofile.objects.create(user=signup)
            data["success"] = "Congratulations! Now You Can Sign In!"
            data["email"] = signup.email
            data["username"] = signup.username
            token = Token.objects.get(user=signup).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

'''