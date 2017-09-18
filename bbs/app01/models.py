from django.db import models

# Create your models here.


from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

class NewsType(models.Model):
    caption = models.CharField(max_length=16)

class News(models.Model):
    title = models.CharField(verbose_name='标题',max_length=32)
    url = models.CharField(verbose_name='URL',max_length=255)
    avatar = models.CharField(verbose_name='头像',max_length=255)
    summary = models.CharField(verbose_name='简介',max_length=255)
    new_type = models.ForeignKey(verbose_name='新闻类型',to="NewsType")
    user = models.ForeignKey(verbose_name='发布者',to='UserInfo',related_name='c')
    ctime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 点赞和评论时，记着更新like_count，comment_count。自增1： F 实现
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    # 查询功能才能使用
    likes = models.ManyToManyField(to='UserInfo',through="Like",through_fields=('nnew','uuser'))

class Comment(models.Model):
    content = models.CharField(verbose_name='评论内容',max_length=255)
    new = models.ForeignKey(verbose_name='评论的新闻ID',to='News')
    user = models.ForeignKey(verbose_name='评论者',to='UserInfo')
    ctime = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)



class Like(models.Model):
    uuser = models.ForeignKey(to='UserInfo',related_name='a')
    nnew = models.ForeignKey(to='News',related_name='b')
    ctime = models.DateTimeField(verbose_name='点赞时间', auto_now_add=True)

    class Meta:
        unique_together = [
            ('uuser','nnew'),
        ]
