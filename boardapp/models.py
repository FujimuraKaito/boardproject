from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    # 画像を保存するための属性
    # pillowというモジュールをインストールしないといけない
    # sudo pip3 install pillow
    images = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    # 既読をした人のユーザーネームを保存する
    readtext = models.CharField(max_length=200, null=True, blank=True, default='a')
