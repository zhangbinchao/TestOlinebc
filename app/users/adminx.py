# users/adminx.py

import xadmin
from xadmin import views
# from .models import EmailVerifyRecord

#xadmin中这里是继承object，不再是继承admin
# class EmailVerifyRecordAdmin(object):
#     # 显示的列
#     list_display = ['code', 'email', 'send_type', 'send_time']
#     # 搜索的字段，不要添加时间搜索
#     search_fields = ['code', 'email', 'send_type']
#     # 过滤
#     list_filter = ['code', 'email', 'send_type', 'send_time']


#主题注册
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

#更改网站标题和公司名注册
class GlobalSetting(object):
    site_title = u"***在线考试系统"
    site_footer = u"power by bc"
    menu_style = "accordion"

xadmin.site.register(views.BaseAdminView, BaseSetting)#主题注册
xadmin.site.register(views.CommAdminView, GlobalSetting)#更改网站标题和公司名注册