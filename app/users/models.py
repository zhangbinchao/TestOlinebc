from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):

    gender_choices = (
        ('male','男'),
        ('female','女'),
    )
    danwei_choices = (
        ('tengxun','腾讯'),
        ('ali','阿里'),
    )
    leibie_choices = (
        ('guanliyuan','管理员'),
        ('danweiguanliyuan','单位管理员'),
        ('kaosheng','考生'),
    )
    zhiwu_choices = (
        ('jingli','经理'),
        ('zhiyuan','职员'),

    )
    nickname = models.CharField(max_length=50, verbose_name=u"姓名", default= "")
    zhiwu = models.CharField('职务',max_length=50,choices=zhiwu_choices,default='')
    birthday = models.DateField('生日',null=True,blank=True)
    gender = models.CharField('性别',max_length=50,choices=gender_choices,default='male')
    leibie = models.CharField('类别',max_length=50,choices=leibie_choices,default='kaosheng')
    danwei = models.CharField('单位',max_length=50,choices=danwei_choices,default='')
    phone = models.CharField('电话',max_length=50,null=True,blank=True)
    image = models.ImageField(upload_to='image/%Y%m',default='image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# class EmailVerifyRecord(models.Model):
#     send_choices = (
#         ('register','注册'),
#         ('forget','找回密码'),
#         ('update_email','修改邮箱')
#     )
#
#     code = models.CharField('验证码',max_length=20)
#     email = models.EmailField('邮箱',max_length=50)
#     send_type = models.CharField(choices=send_choices,max_length=30)
#     send_time = models.DateTimeField(default=datetime.now)
#
#     class Meta:
#         verbose_name = '邮箱验证码'
#         verbose_name_plural = verbose_name


# class Banner(models.Model):
#     title = models.CharField('标题',max_length=100)
#     image = models.ImageField('轮播图',upload_to='banner/%Y%m',max_length=100)
#     url = models.URLField('访问地址',max_length=200)
#     index = models.IntegerField('顺序',default=100)
#     add_time = models.DateTimeField('添加时间',default=datetime.now)
#
#     class Meta:
#         verbose_name = '轮播图'
#         verbose_name_plural = verbose_name