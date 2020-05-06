from django.db import models


class User(models.Model):

    id = models.AutoField('ID', primary_key=True)
    account_name = models.CharField('アカウント名', max_length=255, unique=True)
    username = models.CharField('ユーザー名', max_length=255)
    image = models.ImageField('プロフィール画像', null=True, blank=True)

    def __str__(self):
        return f"{self.id} / {self.username}"

# Create your models here.
