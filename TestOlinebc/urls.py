"""TestOlinebc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
import xadmin
from django.conf.urls import url,include
from django.views.generic import TemplateView
from users.views import LoginView,  RegisterView,userviews,LogoutView
from operation.views import index,PaperListView,PaperView,SelectView,TrainView
from TOBC.views import history
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('login/', LoginView.as_view(),name='login'),
	path('register/', RegisterView.as_view(), name="register"),
	path('captcha/',include('captcha.urls')),
	path('index/', index,name="index"),
	path('paperlist/', PaperListView.as_view(), name="paper_list"),
	path('paper/<paper_id>/', PaperView.as_view(), name="paper"),
	path('select/', SelectView.as_view(), name="select"),
	path('train/', TrainView.as_view(), name="train"),
	path('history/', history, name="history"),
	path('user_center/', userviews, name="user_center"),
	path('logout/', LogoutView.as_view(), name="logout"),

]
