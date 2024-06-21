from django.db import models

# Create your models here.

class BlogPost(models.Model):
    # カテゴリに登録する項目をタプルで定義
    CATEGORY=(('dailylife', '日常のこと'), ('tech', '技術的なこと'), ('hobby', '趣味のこと'))

    title = models.CharField(max_length=200, verbose_name='タイトル')
    content = models.TextField(verbose_name='本文')
    posted_at = models.DateTimeField(verbose_name='投稿時間', auto_now_add=True)
    category = models.CharField(verbose_name='カテゴリー', choices=CATEGORY, max_length=50)

    def __str__(self):
        return self.title