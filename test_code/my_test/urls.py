from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^getPartymemberByid/", views.getPartymemberByid, name="getPartymemberByid"),
    # 登陆
    url(r"^login/", views.login, name="login"),
    url(r"^loginByOpenid/", views.loginByOpenid, name="loginByOpenid"),
    # 党员活动
    url(r"^getPartyactivitiesByPartyid/", views.getPartyactivitiesByPartyid, name="getPartyactivitiesByPartyid"),
    # 志愿者活动
    url(r"^getVolunteerByPartyid/", views.getVolunteerByPartyid, name="getVolunteerByPartyid"),
    # 活动细节
    url(r"^getPartyactivitiesById/", views.getPartyactivitiesById, name="getPartyactivitiesById"),
    # 党员活动报名
    url(r"^partyActivitiesSign/", views.partyActivitiesSign, name="partyActivitiesSign"),
    # 党员活动取消
    url(r"^partyActivitiesUnSign/", views.partyActivitiesUnSign, name="partyActivitiesUnSign"),
    # 志愿活动报名
    url(r"^volunteerSign/", views.volunteerSign, name="volunteerSign"),
    # 志愿活动取消
    url(r"^volunteerUnSign/", views.volunteerUnSign, name="volunteerUnSign"),
    # 党支部留言
    url(r"^doPartymessageLove/", views.doPartymessageLove, name="doPartymessageLove"),
    # 移动课堂
    url(r"^getClassRoomById/", views.getClassRoomById, name="getClassRoomById"),
    url(r"^getClassRoomByPartyId/", views.getClassRoomByPartyId, name="getClassRoomByPartyId"),
    # 支部风采
    url(r"^getBranchStyle/", views.getBranchStyle, name="getBranchStyle"),
    # 支部风采评论
    url(r"^doPartymessageInfo/", views.doPartymessageInfo, name="doPartymessageInfo"),
    # 党员风采评论
    url(r"^doMembermessageInfo/", views.doMembermessageInfo, name="doMembermessageInfo"),
    # 企业
    url(r"^getCompanyByPartyId/", views.getCompanyByPartyId, name="getCompanyByPartyId"),
    url(r"^getCompanyById/", views.getCompanyById, name="getCompanyById"),
    # 考评
    url(r"^getPerformanceByid/", views.getPerformanceByid, name="getPerformanceByid"),
    # 优秀榜
    url(r"^doExcellentLove/", views.doExcellentLove, name="doExcellentLove"),
    url(r"^getExcellentByPartyId/", views.getExcellentByPartyId, name="getExcellentByPartyId"),
    # 党员申请
    url(r"^doPartyRequest/", views.doPartyRequest, name="doPartyRequest"),
    # 党支部信息
    url(r"^getAllParthGroup/", views.getAllParthGroup, name="getAllParthGroup"),
    # 通知公告
    url(r"^getInformationById/", views.getInformationById, name="getInformationById"),
    url(r"^getInformationByPartyid/", views.getInformationByPartyid, name="getInformationByPartyid"),
    # 民主评议
    url(r"^getCommentByPartyid/", views.getCommentByPartyid, name="getCommentByPartyid"),
    # 党员留言
    url(r"^doMembermessageLove/", views.doMembermessageLove, name="doMembermessageLove"),
    # 党员风采
    url(r"^getMemberStyleByPartyId/", views.getMemberStyleByPartyId, name="getMemberStyleByPartyId"),
    # 优秀榜
    url(r"^getgetExcellentById/", views.getgetExcellentById, name="getgetExcellentById"),
    # 党员缴费
    url(r"^CreatePayOrder/", views.CreatePayOrder, name="CreatePayOrder"),
    url(r"^getPartychargeByid/", views.getPartychargeByid, name="getPartychargeByid"),
    # 产品
    url(r"^getGoodsByCompanyId/", views.getGoodsByCompanyId, name="getGoodsByCompanyId"),
    # 招聘
    url(r"^getRecruitByCompanyId/", views.getRecruitByCompanyId, name="getRecruitByCompanyId"),
    # 评议对象
    url(r"^getCommentobjByCommentd/", views.getCommentobjByCommentd, name="getCommentobjByCommentd"),
    # 志愿者活动
    url(r"^getVolunteerById/", views.getVolunteerById, name="getVolunteerById"),
]

