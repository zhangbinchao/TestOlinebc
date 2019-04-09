import xadmin
from xadmin import views
from .models import UserAnswerLog, UserScore


class UserAnswerLogAdmin(object):
    list_display = ['user', 'paper', 'answer','score', 'add_time']
    search_fields = ['user__nick_name', 'user__username', 'paper__paper_name', 'answer', 'score']
    list_filter = ['user', 'paper', 'answer', 'score', 'add_time']


class UserScoreAdmin(object):
    list_display = ['user', 'paper', 'total', 'add_time']
    search_fields = ['user__nick_name', 'user__username', 'paper__paper_name', 'total']
    list_filter = ['user', 'paper', 'total','add_time']


xadmin.site.register(UserAnswerLog, UserAnswerLogAdmin)
xadmin.site.register(UserScore, UserScoreAdmin)