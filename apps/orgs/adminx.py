import xadmin
from .models import City, Org, Teacher


class CityXadmin(object):
    list_display = ['name', 'created_time']


class OrgXadmin(object):
    list_display = ['name', 'image', 'course_num', 'study_num', 'fav_num', 'versit_num', 'category', 'city']


class TeacherXadmin(object):
    list_display = ['name', 'avatar', 'work_year', 'work_position', 'work_style', 'age', 'gender', 'fav_num',
                    'versit_num']


xadmin.site.register(City, CityXadmin)
xadmin.site.register(Org, OrgXadmin)
xadmin.site.register(Teacher, TeacherXadmin)
