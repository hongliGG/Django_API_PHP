from django.db import models

from datetime import datetime


# Create your models here.


# 党支部信息
class Onethink_partygroup(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    # 支部名称
    partyname = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="../static/img", null=True, blank=True)
    # 部门介绍
    partydesc = models.TextField(max_length=500)
    company = models.CharField(max_length=150)
    contacter = models.CharField(max_length=30)
    releasesta = models.IntegerField(default=1)
    # 支部管理员uid
    manager_id = models.IntegerField(default=0)


# 党员信息
class Onethink_partymember(models.Model):
    id = models.AutoField(primary_key=True ,max_length=10)
    name = models.CharField(max_length=30)
    title = models.CharField(u'党内职务', max_length=60)
    photo = models.ImageField(upload_to='', null=True, blank=True)
    partyid = models.IntegerField(default=1)
    partyname = models.CharField(max_length=150)
    joindate = models.IntegerField()
    memberage = models.IntegerField(default=0, )
    mobilephone = models.IntegerField()
    releasesta = models.IntegerField(u'发布状态', default=1)
    mail = models.CharField(max_length=30)
    openid = models.CharField(max_length=10)
    password = models.CharField(max_length=30)


# 党员考评
class Onethink_performance(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    memberid = models.IntegerField()
    name = models.CharField(max_length=30)
    partyid = models.IntegerField(default=1)
    month = models.IntegerField()
    performance = models.CharField(max_length=50, default=1)
    releasestate = models.IntegerField(default=0)


# 党员缴费
class Onethink_partycharge(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    memberid = models.IntegerField()
    name = models.CharField(max_length=30)
    partyid = models.IntegerField()
    salary = models.IntegerField()
    percent = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    charge = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    month = models.IntegerField()
    status = models.IntegerField()
    releasesta = models.IntegerField()


# 党员申请
class Onethink_partyrequest(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    requestname = models.CharField(max_length=30)
    cardid = models.CharField(max_length=19)
    mobilephone = models.IntegerField()
    introducer = models.CharField(max_length=30)
    partyid = models.IntegerField()
    partyname = models.CharField(max_length=150)
    requestinfo = models.TextField()
    time = models.DateTimeField(max_length=10)
    releasestate = models.IntegerField()


#  党支部活动
class Onethink_partyactivities(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    topic = models.CharField(u'活动主题', max_length=255)
    activity_info = models.TextField()
    author = models.CharField(max_length=30)
    attend_num = models.IntegerField()
    partyid = models.IntegerField()
    time = models.IntegerField()
    releasestate = models.IntegerField()


# 志愿者活动
class Onethink_volunteer(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    topic = models.CharField(max_length=255)
    activity_info = models.TextField()
    author = models.CharField(max_length=30)
    attend_num = models.IntegerField()
    partyid = models.IntegerField()
    time = models.IntegerField()
    # 状态
    releasestate = models.IntegerField(default="0")


# 通知公告
class Onethink_information(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    topic = models.CharField(max_length=255)
    activity_info = models.TextField()
    author = models.CharField(max_length=30)
    attend_num = models.IntegerField()
    partyid = models.IntegerField()
    time = models.IntegerField()
    releasestate = models.IntegerField()


# 人员统计
class Onethink_collectnum(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    type = models.CharField(max_length=20)
    external_id = models.IntegerField()
    memberid = models.IntegerField()
    created_time = models.DateTimeField(default=datetime.now)


# 民主评审-主表
class Onethink_comment(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    topic = models.CharField(max_length=255)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    partyid = models.IntegerField()
    releasestate = models.IntegerField()


# 民主评议-评议对象
class Onethink_commentobj(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    external_id = models.IntegerField()
    memberid = models.IntegerField()
    membername = models.CharField(max_length=50)


#  民主评议-评议记录
class Onethink_commentrec(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    external_id = models.IntegerField()
    performance = models.CharField(max_length=50)
    memberid = models.IntegerField()
    membername = models.CharField(max_length=255)
    created_time = models.DateTimeField(default=datetime.now)


# 移动课堂管理
class Onethink_mobileclassroom(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    type = models.IntegerField()
    topic = models.CharField(max_length=255)
    releasestate = models.IntegerField()
    author = models.CharField(max_length=30)
    time = models.IntegerField()
    partyid = models.IntegerField()


# 优秀榜
class Onethink_excellent(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    name = models.CharField(max_length=30)
    story = models.TextField()
    photo = models.ImageField(upload_to='')
    author = models.CharField(max_length=30)
    time = models.IntegerField()
    partyid = models.IntegerField()
    releasestate = models.IntegerField()


# 支部风采
class Onethink_branchstyle(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    partyid = models.IntegerField()
    partyname = models.CharField(max_length=255)
    lovesum = models.IntegerField()
    messagesum = models.IntegerField()


# 支部留言
class Onethink_partymessage(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    memberid = models.IntegerField()
    membername = models.CharField(max_length=255)
    message = models.TextField(u"留言内容")
    time = models.IntegerField()
    status = models.IntegerField()
    partyid = models.IntegerField()


# 党员风采
class Onethink_memberstyle(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    memberid = models.IntegerField()
    membername = models.CharField(max_length=255)
    info = models.TextField(u"个人简介")
    lovesum = models.IntegerField()
    discuss = models.IntegerField()
    releasestate = models.IntegerField()


# 党员留言
class Onethink_membermessage(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    memberid = models.IntegerField()
    membername = models.CharField(max_length=255)
    message = models.TextField(u"留言")
    time = models.IntegerField()
    status = models.IntegerField()
    partyid = models.IntegerField()
    memberstyleid = models.IntegerField()


# 企业之窗
class Onethink_company(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    photo = models.ImageField(upload_to='')
    name = models.CharField(max_length=255)
    info = models.TextField(u"企业名字")
    type = models.CharField(max_length=255)
    scope = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    linkman = models.CharField(max_length=255)
    weixin = models.ImageField(upload_to='')
    contact = models.CharField(max_length=255)
    partyid = models.IntegerField()
    partyname = models.CharField(max_length=255)
    releasestate = models.IntegerField()


# 产品
class Onethink_goods(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    photo = models.ImageField(upload_to='')
    name = models.CharField(max_length=255)
    info = models.TextField(u"产品介绍")
    price = models.IntegerField()
    companyid = models.IntegerField()
    companyname = models.CharField(max_length=255)
    partyid = models.IntegerField()
    releasestate = models.IntegerField()


# 招聘
class Onethink_recruit(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    position = models.CharField(max_length=255)
    jobrequire = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    companyid = models.IntegerField()
    companyname = models.CharField(max_length=255)
    partyid = models.IntegerField()
    releasestate = models.IntegerField()

