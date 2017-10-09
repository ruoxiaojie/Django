from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)


class NewsType(models.Model):
    caption = models.CharField(max_length=16)


class News(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='URL', max_length=255)
    avatar = models.CharField(verbose_name='头像', max_length=255)
    summary = models.CharField(verbose_name='简介', max_length=255)
    new_type = models.ForeignKey(verbose_name='新闻类型', to="NewsType")
    ctime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    '''自增F'''
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    promulgator = models.ForeignKey(verbose_name='发布者', to='UserInfo', related_name='p')
    likes = models.ManyToManyField(to='UserInfo', through="Like", through_fields=('news', 'user',))


class Comment(models.Model):
    content = models.CharField(verbose_name='评论内容', max_length=255)
    ctime = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    comment_new = models.ForeignKey(verbose_name='评论的新闻ID', to='News')
    commenter = models.ForeignKey(verbose_name='评论者', to='UserInfo')


class Like(models.Model):
    user = models.ForeignKey(to='UserInfo', related_name='good_user')
    news = models.ForeignKey(to='News', related_name='good_news')
    ctime = models.DateTimeField(verbose_name='点赞时间', auto_now_add=True)

    class Meta:
        unique_together = [
            ('user', 'news'),
        ]