from . import views
from rest_framework.routers import SimpleRouter
from django.urls import path
#DRF Router
router = SimpleRouter(trailing_slash=False)

# Api for weekly report graph
# router.register('weeklyreportgraph', views.weeklyreportgraph)

#to see frontend view
urlpatterns = [
    path('', views.testoutput, name='testoutput'),
]
