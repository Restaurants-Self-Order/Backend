# Django imports
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

# python imports
from datetime import datetime, timedelta, timezone, date
from dateutil.relativedelta import relativedelta

# DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# Serializer Class imports
from .serializers import WeeklGraphSerializer

# Model Class imports
from .models import Category, Item
from v1.partner.models import PartnerApplication, Partner

# latest 5 applications
def latestApps(request):
    latestApps = PartnerApplication.objects.all().order_by('-created_at')[:5]

# application counts to disply on dashboard 
def displayStatus(request):
    totalApps = PartnerApplication.objects.all().count()
    triagedApps = PartnerApplication.objects.filter(status=Triaged).count()
    completedApps = PartnerApplication.objects.filter(status=Completed).count()
    pendingApps = PartnerApplication.objects.filter(status=Pending).count()

# weekly report graph
def weeklyReportGraph(request):
    today = Mymodel.objects.filter(created_at=datetime.now())
    week = Mymodel.objects.filter(created_at=datetime.now()-timedelta(days=7)).count()
    month = Mymodel.objects.filter(created_at=datetime.now()-timedelta(days=30)).count()
    
    #graph data
    labels = []
    data = []

    queryset = PartnerApplication.objects.filter(created_at=datetime.now()-timedelta(days=7)).order_by('-created_at')
    #testing
    for p in queryset:
        labels.append(p.object)
        data.append(p.object)