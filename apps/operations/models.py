from django.db import models
from datetime import datetime
from users.models import UserProfile
from courses.models import Course


# Create your models here.
class UserAsk(models.Model):
    name = models.CharField(max_length=30, verbose_name='姓名')
    phone = models.CharField(max_length=11, verbose_name='手机')
    course = models.CharField(max_length=20, verbose_name='课程')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '咨询信息'
        verbose_name_plural = verbose_name


class UserFav(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='收藏用户', on_delete=models.CASCADE)
    fav = models.IntegerField(verbose_name='收藏ID')
    fav_type = models.IntegerField(choices=((1, 'org'), (2, 'course'), (3, 'teacher')), verbose_name='收藏类别')
    fav_status = models.BooleanField(default=False, verbose_name='收藏状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '收藏信息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='学习用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='学习课程', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('user', 'course')
        verbose_name = '用户学习课程信息'
        verbose_name_plural = verbose_name


class UserComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='评论用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='评论课程', on_delete=models.CASCADE)
    content = models.CharField(max_length=300, verbose_name='评论内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    message_man = models.IntegerField(default=0, verbose_name='消息用户')
    content = models.CharField(max_length=300, verbose_name='消息内容')
    message_status = models.BooleanField(default=False, verbose_name='消息状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name
