# Django imports
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
import datetime
# DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
# Serializer Class imports
from .serializers import CategorySerializer, ItemSerializer
# Model Class imports
from .models import Category, Item
from v1.shop.models import Shop
#importing pagination
from .paginations import SmallOffsetPagination, SmallPagesPagination

# APIs for category and Item
@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'Category List':'/category-list',
    'Category Detail View':'/category-detail/<str:pk>',
    'Category Create':'/category-create',
    'Category Update':'/category-update/<str:pk>',
    'Category Delete':'/category-delete/<str:pk>',

    'ItemList':'/item-list',
    'Item Detail View':'/item-detail/<str:pk>',
    'Item Create':'/item-create',
    'Item Update':'/item-update/<str:pk>',
    'Item Delete':'/item-delete/<str:pk>',
    }
  return Response(api_urls)

# methods for category 
# categoryList
class CategoryList(generics.ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [IsAuthenticated]
  pagination_class = SmallPagesPagination

# categoryDetail
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def categoryDetail(request, pk):
  category = Category.objects.get(id=pk)
  serializer = CategorySerializer(category, many=False)
  return Response(serializer.data)

# categoryCreate
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def categoryCreate(request):  
  serializer = CategorySerializer(data=request.data)
  data={}
  if serializer.is_valid():
    serializer.save(user=request.user, shop=request.user.shop)
    data["success"] = "Category Has Been Created!"
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# categoryUpdate
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def categoryUpdate(request, pk):
  category = Category.objects.get(id=pk)
  user = request.user
  if category.user != user:
    return Response({'Response':"You dont have Permission to edit this data."})
  serializer = CategorySerializer(instance=category, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

# categoryDelete
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def categoryDelete(request, pk):
  category = Category.objects.get(id=pk)
  user = request.user
  if category.user != user:
    return Response({'Response':"You dont have Permission to delete this data."})
  category.delete()
  return Response('Category Has Been Deleted!')

# Item List
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def itemList(request):
  try:
    items = Item.objects.all().order_by('-id')
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == "GET":
    serializer = ItemSerializer(items, many=True)
  return Response(serializer.data)

class ItemList(generics.ListAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permission_classes = [IsAuthenticated]
  pagination_class = SmallPagesPagination

# Single Item Details
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def itemDetail(request, pk):
  try:
    item = Item.objects.get(id=pk)
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = ItemSerializer(item, many=False)
  return Response(serializer.data)

# Item Create
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def itemCreate(request):
  if request.method == "POST":
    shop=request.user.shop
    print(shop)
    serializer = ItemSerializer(data=request.data)
    data={}
    if serializer.is_valid():
      serializer.save(user=request.user, shop=request.user.shop, date_added=datetime.datetime.now())
      data["success"]="Create Successful"
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Item Update
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def itemUpdate(request, pk):
  try:
    item = Item.objects.get(id=pk)
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == "POST":
    user = request.user
    if item.user != user:
      return Response({'Response':"You dont have Permission to edit this data."})
    serializer = ItemSerializer(instance=item, data=request.data)
    data={}
    if serializer.is_valid():
      serializer.save()
      data["success"]="Item Has Been Updated"
      return Response (data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Item Delete
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def itemDelete(request, pk):
  try:
    item = Item.objects.get(id=pk)
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "DELETE":
    user = request.user
    if item.user != user:
      return Response({'Response':"You dont have Permission to delete this data."})
    item.delete()
    return Response('Category Has Been Deleted!')