import xadmin
from .models import *


# Create your models here.
class CourseXadmin(object):
    list_display = ['image','name','study_num','level','fav_num','category','teacher','org']



class LessonXadmin(object):
    list_display = ['name','course','created_time']



class VideoXadmin(object):
    list_display = ['name', 'study_time', 'url']



class SourceXadmin(object):
    list_display = ['name', 'course', 'created_time']

xadmin.site.register(Course,CourseXadmin)
xadmin.site.register(Lesson,LessonXadmin)
xadmin.site.register(Video,VideoXadmin)
xadmin.site.register(Source,SourceXadmin)