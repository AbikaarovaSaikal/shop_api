from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer, UserAuthSerializer, UserConfirmCodeSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import ConfirmCode
import random

@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = User.objects.create_user(username=username, 
                                    password=password,
                                    is_active=False)
    
    code = str(random.randint(100000, 999999))
    ConfirmCode.objects.create(user=user, code=code)
    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id': user.id})

@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = authenticate(username=username, password=password)

    if user and user.is_active:
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def confirm_user_api_view(request):
    serializer = UserConfirmCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user_id = serializer.validated_data['user_id']
    code = serializer.validated_data['code']

    confirm = ConfirmCode.objects.filter(user_id=user_id, code=code).first()
    if not confirm:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    user = confirm.user
    user.is_active = True
    user.save()
    confirm.delete()

    return Response({'status': 'confirm'})