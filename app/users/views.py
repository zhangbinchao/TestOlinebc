from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm,  UserInfoForm

# Create your views here.
from django.contrib.auth import authenticate, login,logout
from django.views.generic.base import View
from .models import UserProfile
from django.contrib.auth.hashers import make_password

title = "在线考试系统"
phoneNumber = "123"

#调试完成
class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, "login.html", {"login_form":login_form, "title": title, "phoneNumber": phoneNumber})

    def post(self, request):
        print(1)
        login_form = LoginForm(request.POST)

        if login_form.is_valid():#验证表是否为空
            print(3)
            user_name = request.POST.get("username", "")
            print(4)
            user_password = request.POST.get("password", "")
            print(user_name)
            user = authenticate(username=user_name, password=user_password)
            print(user)
            if user is not None:
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误","login_form": login_form})
        else:
            return render(request, "login.html", {"login_form": login_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "login.html", {"msg":u"您已经成功退出登录状态", })

class RegisterView(View):
    """注册模块,调试完成"""
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form, "title": title})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if request.method == 'POST':
            if register_form.is_valid():
                user_name = request.POST.get("username", "")#账号

                if UserProfile.objects.filter(username=user_name):
                    return render(request, "register.html",
                                {"title": title,"register_form": register_form, "msg": u"该考号已经被注册"});

                user_password = request.POST.get("password", "")
                user_nickname = request.POST.get("nickname", "")
                user_danwei = request.POST.get("danwei", "")
                user_zhiwu = request.POST.get("zhiwu", "")

                user_profile = UserProfile()
                user_profile.username = user_name
                user_profile.nickname = user_nickname
                user_profile.danwei = user_danwei
                user_profile.zhiwu = user_zhiwu
                user_profile.is_active = True
                user_profile.password = make_password(user_password)
                user_profile.save()
                return render(request, "register.html", {"title": title,"msg":u"注册成功"})
            else:
                return render(request, "register.html",{"register_form":register_form, "title": title})
        else:
            form = UserInfoForm(
		        initial={

			        'danwei':'腾讯',
			        'zhiwu': '经理',
		        }
	        )
            return render(request, "register.html", {"register_form": form, "title": title})


def userviews(request):
    user_form = UserInfoForm(request.POST)
    user = UserProfile.objects.get(username=request.user)
    if request.method == 'POST':
        if user_form.is_valid():
            nick_name = user_form.cleaned_data['nick_name']
            birthday = user_form.cleaned_data['birthday']
            gender = user_form.cleaned_data['gender']
            # leibie = user_form.cleaned_data['leibie']
            danwei = user_form.cleaned_data['danwei']
            zhiwu = user_form.cleaned_data['zhiwu']

            user.nickname = nick_name
            user.birthday = birthday
            user.gender = gender
            # user.leibie = leibie
            user.danwei = danwei
            user.zhiwu = zhiwu
            user.save()
            message = '修改成功'
            return redirect('/user_center/')
        else:
            message = '修改失败'
            user_form = UserInfoForm()
            return render(request, 'usercenter-info.html',{'Edit_FormInput':user_form})
    else:
        nick_name = user.nickname
        birthday = user.birthday
        gender = user.gender
        # leibie = user.leibie
        danwei = user.danwei
        zhiwu = user.zhiwu
        form = UserInfoForm(
            initial={
	            'nick_name' : nick_name,
	            'birthday' : birthday,
	            'gender': gender,
	            # 'leibie': leibie,
	            'danwei': danwei,
	            'zhiwu': zhiwu,
            }
        )
        return render(request, 'usercenter-info.html', {'Edit_FormInput':form})

#404调试完成
def page_not_found(request):
    # 全局404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {"title": title})
    response.status_code = 404
    return response


#500调试完成
def page_error(request):
    # 全局500处理函数
    from django.shortcuts import render_to_response
    response=render_to_response('500.html', {"title":title});
    response.status_code = 500
    return response
