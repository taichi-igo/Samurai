from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from datetime import datetime

from user.models import User
from tweet.models import Tweet, Comment
from tweet.serializers import TweetSerializer, CommentSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

from copy import copy

class TweetViewSet(viewsets.ModelViewSet):

    queryset = Tweet.objects.all()#.order_by('created_at')
    serializer_class = TweetSerializer


    # tweets/  GET
    def list(self, request):
        query = Tweet.objects.all()#.order_by('created_at')
        data = TweetSerializer(query, many=True).data
        return Response(data)


    # tweets/  POST
    def create(self, request):

        try :
            post_data = copy(request.POST)
            user_id = post_data.pop('user_id')
            user = User.objects.get(id=int(user_id[0]))
            tweet = Tweet.objects.create(**post_data, user_id=user)
            data = TweetSerializer(tweet).data
            return Response(data, status=status.HTTP_201_CREATED)

        except Exception as error :
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)


    # tweets/:id/  GET
    def retrieve(self, request, pk=None):

        try :
            tweet = Tweet.objects.get(id=pk)
            data = TweetSerializer(tweet).data
            return Response(data)

        except ObjectDoesNotExist :
            return Response('このユーザーは存在しません', status=status.HTTP_404_NOT_FOUND)



    # tweets/:id/　PUT
    def update(self, request, pk=None):

        try :
            tweet = Tweet.objects.get(id=pk)
            tweet.text = 'I am father.'
            tweet.save()
            data = TweetSerializer(tweet).data
            return Response(data)

        except ObjectDoesNotExist :
            return Response('このユーザーは存在しません', status=status.HTTP_404_NOT_FOUND)


    # tweets/:id/　DELETE
    def destroy(self, request, pk=None):
        try :
            tweet = Tweet.objects.get(id=pk)
            tweet.delete()
            data = TweetSerializer(tweet).data
            return Response(data)

        except ObjectDoesNotExist :
            return Response('このユーザーは存在しません', status=status.HTTP_404_NOT_FOUND)

    @action(methods=['post'], detail=True)
    def like(self, request, pk=None):
        me = User.objects.get(id=1)
        tweet = Tweet.objects.get(id=pk)

        # すでにいいねしている場合
        if me in tweet.liked_users.all() :
            tweet.liked_users.remove(me)

        # いいねしてない場合
        else :
            tweet.liked_users.add(me)

        data = TweetSerializer(tweet).data
        return Response(data)



class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()#.order_by('created_at')
    serializer_class = CommentSerializer

    # comments/  GET
    def list(self, request):
        query = Comment.objects.all()#.order_by('created_at')
        data = CommentSerializer(query, many=True).data
        return Response(data)





# Create your views here.
