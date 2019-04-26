import xadmin
from .models import Banner, EmailVerifyCode
from xadmin import views


# 配置xadmin主题，注册的时候要用view去使用
class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalXadminSetting(object):
    site_title = '谷粒教育后台管理系统'
    site_footer = '尚硅谷教育公司'
    menu_style = 'accordion'


class BannerXadmin(object):
    list_display = ['image', 'url', 'created_time']
    search_fields = ['image', 'url']
    list_filter = ['image', 'url']


class EmailVerifyCodeXadmin(object):
    list_display = ['code', 'email', 'send_type', 'created_time']


xadmin.site.register(Banner, BannerXadmin)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeXadmin)
# 注册主题类
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
# 注册全局样式类
xadmin.site.register(views.CommAdminView, GlobalXadminSetting)
