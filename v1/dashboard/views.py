# Django imports
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.utils.timezone import make_aware
from django.db.models import Count
from django.db.models import Q
#for sql queries
from django.db import connection

# python imports
from datetime import datetime, timedelta, timezone, date
from dateutil.relativedelta import relativedelta
import pytz
# DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# Serializer Class imports
from .serializers import WeeklGraphSerializer

# Model Class imports
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

# Converting data into dictionary
def dictfetchall(cursor):
    desc = cursor.description
    return[
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
    
def testoutput(request):
    cursor = connection.cursor()
    current_date=datetime.today().strftime("%Y-%m-%d")
    current_date1=datetime.today()
    current_date_7days=current_date1+timedelta(days=7)
    current_date_7days=current_date_7days.strftime("%Y-%m-%d")
    
    app_all = PartnerApplication.objects.filter(created_at__range=[current_date,current_date_7days])

    app_dates = PartnerApplication.objects.order_by().values("created_at__date").distinct()
    total_apps_a_day_list = []
    day_name_list =[]

    day_name_list.append(app_dates)
    for app in app_dates:
        access_date=app["created_at__date"]
        datacount = PartnerApplication.objects.filter(created_at__date=access_date).count()
        datadate = PartnerApplication.objects.filter(created_at__date=access_date)
        total_apps_a_day_list.append({"date":access_date,"count":datacount})
    # print(data)
    return render(request,'output.html',{'count': total_apps_a_day_list })



# weekly report graph   
def weeklyReportGraph(request):
    cursor = connection.cursor()
    current_date=datetime.today().strftime("%Y-%m-%d")
    current_date1=datetime.today()
    current_date_7days=current_date1+timedelta(days=7)
    current_date_7days=current_date_7days.strftime("%Y-%m-%d")
    
    app_all = PartnerApplication.objects.filter(created_at__range=[current_date,current_date_7days])

    app_dates = PartnerApplication.objects.order_by().values("created_at__date").distinct()
    total_apps_a_day_list = []
    day_name_list =[]

    day_name_list.append(app_dates)
    for app in app_dates:
        access_date=app["created_at__date"]
        datacount = PartnerApplication.objects.filter(created_at__date=access_date).count()
        datadate = PartnerApplication.objects.filter(created_at__date=access_date)
        total_apps_a_day_list.append({"date":access_date,"count":datacount})
    # print(data)
    return render(request,'output.html',{'count': total_apps_a_day_list })
    
# dont delete these queries
# now = timezone.now()
# current_date=datetime.today().strftime("%Y-%m-%d")
# current_date1=datetime.today()
# current_date_7days=current_date1+timedelta(days=7)
# current_date_7days=current_date_7days.strftime("%Y-%m-%d")
# today = Mymodel.objects.filter(created_at=datetime.now())
# week = Mymodel.objects.filter(created_at=datetime.now()-timedelta(days=7)).count()
# month = Mymodel.objects.filter(created_at=datetime.now()-timedelta(days=30)).count()