from django.db import models

class Task(models.Model):
    id = models.AutoField('ID', primary_key=True, null=False)
    title = models.CharField('タイトル', max_length = 255)
    detail = models.TextField('詳細')
    is_done = models.BooleanField('完了フラグ', default = False)

    def __str__(self):
        return f"{self.id} / {self.title}"


class Label(models.Model):
    id = models.AutoField('ID', primary_key=True, null=False)
    label = models.CharField('ラベル', max_length = 255)
    is_done = models.BooleanField('完了フラグ', default = False)

    def __str__(self):
        return f"{self.id} / {self.label}"
# Create your models here.
