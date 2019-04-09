import xadmin
from xadmin import views
from .models import CourseList,Question, Paper,PaperList


class CourseListAdmin(object):
    list_display = ['name', 'decs', 'add_time']
    search_fields = ['name', 'decs']
    list_filter = ['name', 'decs', 'add_time']

class QuestionAdmin(object):
    list_display = ['course','questionType', 'score', 'content', 'answer', 'choice_a', 'choice_b',
                    'choice_c', 'choice_d', 'note', 'boolt', 'boolf', 'add_time']
    search_fields = ['course__name','questionType', 'content', 'answer', 'choice_a', 'choice_b',
                     'choice_c', 'choice_d', 'note', 'boolt', 'boolf']
    list_filter = ['course','questionType', 'score', 'content', 'answer', 'choice_a',
                   'choice_b', 'choice_c', 'choice_d', 'note', 'boolt', 'boolf','add_time']

class PaperListAdmin(object):
    list_display = ['id','course','name', 'is_allow', 'add_time']
    search_fields = ['id','course__name', 'name', 'is_allow']
    list_filter = ['id','course','name', 'is_allow', 'add_time']

class PaperAdmin(object):
    list_display = ['course', 'paper_name', 'question', 'add_time']
    search_fields = ['course__name', 'paper_name__name', 'paper_name__id', 'paper_name__is_allow', 'question__id',
                     'question__content', 'question__answer']
    list_filter = ['course', 'paper_name', 'question__id', 'question__content','add_time','paper_name__name',]

xadmin.site.register(CourseList, CourseListAdmin)
xadmin.site.register(Question, QuestionAdmin)
xadmin.site.register(PaperList, PaperListAdmin)
xadmin.site.register(Paper, PaperAdmin)