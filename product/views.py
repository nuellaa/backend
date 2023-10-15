from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import food
from rest_framework import serializers
# from django.http import HttpResponse

# Create your views here.

class FoodSerializer(serializers.ModelSerializer):
 class Meta:
  model = food
  fields = '__all__'

@api_view(['Get'])
def hello(request):
 allfood = food.objects.all()

 serializers = FoodSerializer(allfood, many = True)

 return Response(serializers.data)
#  print(allfood)
 return Response(allfood)

@api_view(['POST'])
def Create_food(request):
 print(request.data)
 return Response("The title is",)


