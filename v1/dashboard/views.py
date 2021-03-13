# Django imports
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Count

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
    start_date = PartnerApplication.objects.filter(created_at=datetime.now())
    end_date = PartnerApplication.objects.filter(created_at=datetime.now()-timedelta(days=7))
    
    # weekendData = PartnerApplication.objects.values('uuid').filter(created_at__range=(start_date, end_date)).annotate(count=Count('uuid')).order_by('-created_at')
    weekendData = PartnerApplication.objects.values('created_at').annotate(number_of_applications=Count('created_at', filter(created_at__range=(start_date, end_date)))).order_by('-created_at')
    
    #graph data
    labels = [] #day name
    appsPerDay = [] #count app based on created_at

    categories = list()
    survived_series_data = list()
    not_survived_series_data = list()

    #inserting data into collection
    for entry in weekendData:
        labels.append(entry['created_at'])
        appsPerDay.append(entry['number_of_applications'])

# dont delete these queries
# queryset = PartnerApplication.objects.raw('SELECT * FROM partner_application')
# today = Mymodel.objects.filter(created_at=datetime.now())
# week = Mymodel.objects.filter(created_at=datetime.now()-timedelta(days=7)).count()
# month = Mymodel.objects.filter(created_at=datetime.now()-timedelta(days=30)).count()