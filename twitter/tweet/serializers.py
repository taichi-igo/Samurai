from rest_framework import serializers
from tweet.models import Tweet, Comment
from user.serializers import UserSerializer

class TweetSerializer(serializers.ModelSerializer):

    liked_num = serializers.IntegerField()
    user_id = UserSerializer()

    class Meta:
        model = Tweet
        # fields = '__all__'
        fields = (
            'id',
            'text',
            'user_id',
            'liked_num',
            'liked_users',
        )

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        # fields = (
        #     'id',
        #     'text',
        #     'user_id',
        #
        # )
