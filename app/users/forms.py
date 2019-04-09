from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    #与前台表格的name相同
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class RegisterForm(forms.Form):
    zhiwu_choices = (
		('jingli', '经理'),
		('zhiyuan', '职员'),

	)
    danwei_choices = (
		('tengxun', '腾讯'),
		('ali', '阿里'),
	)


    username = forms.IntegerField(min_value=1000000, max_value=9999999)
    # email = forms.EmailField(required=True)
    nickname = forms.CharField(required=True, max_length=10)
    password = forms.CharField(required=True, min_length=5)
    danwei = forms.ChoiceField(label='所在单位',choices=danwei_choices, required=True)
    zhiwu = forms.ChoiceField( label='本人职务', choices=zhiwu_choices, required=True)
    # captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class UserInfoForm(forms.Form):
    gender_choices = (
		('male', '男'),
		('female', '女'),
	)
    danwei_choices = (
	    ('tengxun', '腾讯'),
	    ('ali', '阿里'),
    )

    leibie_choices = (
	    ('guanliyuan', '管理员'),
	    ('danweiguanliyuan', '单位管理员'),
	    ('kaosheng', '考生'),
    )
    zhiwu_choices = (
	    ('jingli', '经理'),
	    ('zhiyuan', '职员'),

    )
    nick_name = forms.CharField(label='姓    名',required=True, max_length=50)
    birthday = forms.DateField(label='生    日',required=True)
    gender = forms.ChoiceField(label='性    别',choices=gender_choices, required=True)
    # leibie = forms.ChoiceField(label='人员类别',choices=leibie_choices, required=True)
    danwei = forms.ChoiceField(label='所在单位',choices=danwei_choices, required=True)
    zhiwu = forms.ChoiceField( label='本人职务', choices=zhiwu_choices, required=True)
