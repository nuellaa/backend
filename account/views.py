from django.shortcuts import render
from rest_framework.response import Response
from  rest_framework.decorators import api_view
from .serializer import userCreateSerializer, LoginSerializer
from rest_framework import status
# Create your views here.




@api_view(['POST'])
def signup(request):

    try:

        new_user = userCreateSerializer(data=request.data)

        if new_user.is_valid():
            new_user.save()
            return Response(new_user.data, status=status.HTTP_200_OK)
        else:
            return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)

    except BaseException as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def Login(request):
    try:
        user = LoginSerializer(data=request.data)

        if user.is_valid():
            result = user.login(user.data)
            return Response(result)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

    except BaseException as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)