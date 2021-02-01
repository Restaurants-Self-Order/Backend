# Django imports
from django.shortcuts import render
from django.http import JsonResponse
# DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token