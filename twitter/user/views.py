from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from datetime import datetime

from user.models import User
from user.serializers import UserSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

# @action(detail=False, method=['get'])
# def user_list(request):
#     return Response('@@@ user list @@@')


# # class UserViewSet(viewsets.ModelViewSet):
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer



    # users/  GET
    def list(self,request):
        query = User.objects.all()
        data = UserSerializer(query, many=True).data
        return Response(data)

    # users/  POST
    def create(self,request):

        try:
            user = User.objects.create(**request.POST)
            print('OK')
            data = UserSerializer(user).data
            return Response(data, status=status.HTTP_201_CREATED)

        except Exception as error:
            # return Response('すでにこのアカウント名のユーザーは存在します', status=status.HTTP_400_BAD_REQUEST)
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)

    # users/:id/  GET
    def retrieve(self, request, pk=None):
        try:
            query = User.objects.get(id=pk)
            data = UserSerializer(query).data
            return Response(data)

        except ObjectDoesNotExist:
            return Response('ユーザーデータが存在しません', status=status.HTTP_404_NOT_FOUND)


    # users/:id/　PUT
    def update(self, request, pk=None):
        try:
            query = User.objects.get(id=pk)
            query.username = 'father'
            query.save()
            data = UserSerializer(query).data
            return Response(data)

        except ObjectDoesNotExist:
            return Response('ユーザーデータが存在しません', status=status.HTTP_404_NOT_FOUND)


    # users/:id/　DELETE
    def destroy(self, request, pk=None):
        try:
            query = User.objects.get(id=pk)
            query.delete()
            data = UserSerializer(query).data
            return Response(data)

        except ObjectDoesNotExist:
            return Response('ユーザーデータが存在しません', status=status.HTTP_404_NOT_FOUND)

# Create your views here.
