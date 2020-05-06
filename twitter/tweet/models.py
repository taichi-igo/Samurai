from django.db import models
from user.models import User
from datetime import datetime

class Tweet(models.Model):

        id = models.AutoField('ID', primary_key=True)
        text = models.CharField('ツイート内容', max_length=140)
        user_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user')
        liked_users = models.ManyToManyField(User, null=True, blank=True, related_name='liked_users')
        created_at = models.DateTimeField('現在の時刻', default=datetime.now())

        @property
        def liked_num(self):
            return self.liked_users.count()

        def __str__(self):
            return f"{self.id} / {self.text}"



class Comment(models.Model):

        id = models.AutoField('ID', primary_key=True)
        tweet_id = models.ForeignKey(Tweet, on_delete=models.PROTECT)
        user_id = models.ForeignKey(User, on_delete=models.PROTECT)
        text = models.CharField('コメント', max_length=140)
        created_at = models.DateTimeField('現在の時刻', default=datetime.now())

        def __str__(self):
            return f"{self.id} / {self.text}"





# Create your models here.
