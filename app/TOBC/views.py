from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from operation.models import  UserScore
from users.models import UserProfile


def history(request):
	if request.user.is_authenticated:
		user_info = UserProfile.objects.get(username=request.user)
		if user_info.leibie =='danweiguanliyuan':
			hiss = UserScore.objects.all()
		else:
			hiss = UserScore.objects.filter(user=request.user)
		return render(request, 'history.html', locals())
	else:
		return render(request, "login.html", {"msg": u'为保护用户信息，不对未登录用户开放'})
