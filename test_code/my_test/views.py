from django.views.decorators.http import require_POST
from django.core import serializers
from django.http import JsonResponse, HttpResponse
import json
from . import models


# Create your views here.


def response(data):
    response = HttpResponse(data)
    data_list = []
    dict_list = {}
   
    for x in response:
        json_data = list(eval(x.decode()))
        
        for datas in json_data:
            pk = datas.get("fields")
            pk["id"] = datas.get("pk")
            data_list.append(datas.get("fields"))
    dict_list["list"] = data_list
    return {"data":dict_list}


# loginByOpenid
@require_POST
def loginByOpenid(request):
    req = json.loads(request.body)
    print(req)
    openid = req.get("openid")
    print(openid)
    data =serializers.serialize("json", models.Onethink_partymember.objects.filter(openid=openid))
    print(data)
    response = HttpResponse(data)
    # dict_list = {}
    json_data = None
    for x in response:
        json_data = eval(x.decode())
        for datas in json_data:
            pk = datas.get("fields")
            pk["id"] = datas.get("pk")
            json_data = json_data[0].get("fields")
    ret = {}
    if data == None:
        ret['ret'] = -1
    else:
        ret = {
            'ret' : 0,
            'data' : json_data
        }
    # dict_list = response(data)
    return JsonResponse(ret, safe=False)


# 登陆
def login(request):
    req = json.loads(request.body)
    mobilephone = req.get("mobilephone")
    password = req.get("password")
    openid = req.get("openid")
    data = serializers.serialize("json", models.Onethink_partymember.objects.filter(mobilephone=mobilephone,
                                                                                        password=password,
                                                                                        openid=openid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 党员活动
@require_POST
def getPartyactivitiesByPartyid(request):
    req = json.loads(request.body)
    # print(req)
    partyid = req.get("partyid") 
    data = serializers.serialize("json", models.Onethink_partyactivities.objects.filter(partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 志愿者活动
@require_POST
def getVolunteerByPartyid(request):
    req = json.loads(request.body)
    partyid = req.get("partyid")
    data = serializers.serialize("json", models.Onethink_volunteer.objects.filter(partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


@require_POST
def getPartymemberByid(request):
    req = json.loads(request.body)
    id = req.get("id")
    data = serializers.serialize("json", models.Onethink_partymember.objects.filter(id=id))
    response = HttpResponse(data)
    json_data = None
    for x in response:
        json_data = eval(x.decode())
        for datas in json_data:
            pk = datas.get("fields")
            pk["id"] = datas.get("pk")
            json_data = json_data[0].get("fields")
    ret = {}
    if data == None:
        ret['ret'] = -1
    else:
        ret = {
            'ret': 0,
            'data': json_data
        }
    return JsonResponse(ret, safe=False)


# 活动细节
@require_POST
def getPartyactivitiesById(request):
    req = json.loads(request.body)
    print(req)
    id = req.get("id")
    # memberid = req.get("memberid")
    data = serializers.serialize("json", models.Onethink_partyactivities.objects.filter(id=id))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 党员活动报名和支援志愿者活动报名
# 党员活动报名
def partyActivitiesSign(request):
    req = json.loads(request.body)
    # memberid = req.get("memberid")
    # membername = req.get("membername")
    partyid = req.get("partyid")
    # partyname = req.get("partyname")
    data = serializers.serialize("json", models.Onethink_partyactivities.objects.filter(partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 党员活动报名取消
def partyActivitiesUnSign(request):
    req = json.loads(request.body)
    # memberid = req.get("memberid")
    # membername = req.get("membername")
    partyid = req.get("partyid")
    # partyname = req.get("partyname")
    data = serializers.serialize("json", models.Onethink_partyactivities.objects.filter(partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 志愿活动报名
def volunteerSign(request):
    req = json.loads(request.body)
    # memberid = req.get("memberid")
    # membername = req.get("membername")
    partyid = req.get("partyid")
    # partyname = req.get("partyname")
    data = serializers.serialize("json", models.Onethink_volunteer.objects.filter(partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 支援活动取消报名
@require_POST
def volunteerUnSign(request):
    req = json.loads(request.body)
    # memberid = req.get("memberid")
    # membername =req.get("membername")
    partyid = req.get("partyid")
    # partyname = req.get("partyname")
    data = serializers.serialize("json", models.Onethink_volunteer.objects.filter(partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# doPartymessageLove 党支部
@require_POST
def doPartymessageLove(request):
    req = json.loads(request.body)
    memberid = req.get("memberid")
    partyid = req.get("partyid")
    data = serializers.serialize("json", models.Onethink_membermessage.objects.filter(memberid=memberid, partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 移动课堂
@require_POST
def getClassRoomById(request):
    req = json.loads(request.body)
    id = req.get("id")
    data = serializers.serialize("json", models.Onethink_mobileclassroom.objects.filter(id=id))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


@require_POST
def getClassRoomByPartyId(request):
    req = json.loads(request.body)
    partyid = req.get("partyid")
    data = serializers.serialize("json", models.Onethink_mobileclassroom.objects.filter(partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 支部风采
@require_POST
def getBranchStyle(request):
    req = json.loads(request.body)
    partyid = req.get("partyid")
    data = serializers.serialize("json", models.Onethink_branchstyle.objects.filter(partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 支部风采评论
@require_POST
def doPartymessageInfo(request):
    req = json.loads(request.body)

    memberid = req.get("memberid")
    membername = req.get("membername")
    message = req.get("message")
    partyid = req.get("partyid")
    data = serializers.serialize("json", models.Onethink_partymessage.objects.filter(memberid=memberid, membername=membername, message=message, partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 党员风采评论
@require_POST
def doMembermessageInfo(request):
    req = json.loads(request.body)

    memberid = req.get("memberid")
    membername = req.get("membername")
    message = req.get("message")
    memberstyleid = req.get("memberstyleid")
    data = serializers.serialize("json", models.Onethink_membermessage.objects.filter(memberid=memberid, membername=membername, message=message, memberstyleid=memberstyleid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 企业
@require_POST
def getCompanyByPartyId(request):
    req = json.loads(request.body)
    partyid = req.get("partyid")
    data = serializers.serialize("json", models.Onethink_membermessage.objects.filter(partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


@require_POST
def getCompanyById(request):
    req = json.loads(request.body)
    id = req.get("id")
    data = serializers.serialize("json", models.Onethink_membermessage.objects.filter(id=id))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 考评
@require_POST
def getPerformanceByid(request):
    req = json.loads(request.body)
    id = req.get("id")
    data = serializers.serialize("json", models.Onethink_performance.objects.filter(id=id))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# doExcellentLove 优秀榜 出错
@require_POST
def doExcellentLove(request):
    req = json.loads(request.body)
    memberid = req.get("memberid")
    excellentid = req.get("excellentid")
    data = serializers.serialize("json", models.Onethink_excellent.objects.filter(memberid=memberid, excellentid=excellentid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)

# 优秀榜
@require_POST
def getExcellentByPartyId(request):
    req = json.loads(request.body)
    partyid = req.get("partyid")
    data = serializers.serialize("json", models.Onethink_excellent.objects.filter(partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 党员申请
@require_POST
def doPartyRequest(request):
    req = json.loads(request.body)
    requestname = req.get("requestname")
    cardid = req.get("cardid")
    mobilephone = req.get("mobilephone")
    introducer = req.get("introducer")
    partyid = req.get("partyid")
    requestinfo = req.get("requestinfo")
    data = serializers.serialize("json", models.Onethink_partyrequest.objects.filter(requestname=requestname, cardid=cardid, \
                                                                                     mobilephone=mobilephone, introducer=introducer, \
                                                                                     requestinfo=requestinfo, partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 党支部信息
@require_POST
def getAllParthGroup(request):
    req = json.loads(request.body)
    id = req.get("id")
    data = serializers.serialize("json", models.Onethink_partygroup.objects.filter(id=id))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 通知公告
@require_POST
def getInformationById(request):
    req = json.loads(request.body)
    id = req.get("id")
    data = serializers.serialize("json", models.Onethink_information.objects.filter(id=id))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


@require_POST
def getInformationByPartyid(request):
    req = json.loads(request.body)
    partyid = req.get("partyid")
    data = serializers.serialize("json", models.Onethink_information.objects.filter(partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 民主评议
@require_POST
def getCommentByPartyid(request):
    req = json.loads(request.body)
    partyid = req.get("partyid")
    data = serializers.serialize("json", models.Onethink_comment.objects.filter(partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# doMembermessageLove 党员留言
@require_POST
def doMembermessageLove(request):
    req = json.loads(request.body)
    memberid = req.get("memberid")
    partyid = req.get("partyid")
    data = serializers.serialize("json",
                                 models.Onethink_membermessage.objects.filter(memberid=memberid, partyid=partyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 党员风采 出错
@require_POST
def getMemberStyleByPartyId(request):
    req = json.loads(request.body)
    memberid = req.get("memberid")
    data = serializers.serialize("json", models.Onethink_memberstyle.objects.filter(memberid=memberid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# getExcellentById 优秀榜
@require_POST
def getgetExcellentById(request):
    req = json.loads(request.body)
    id = req.get("id")
    # memberid = req.get("memberid")
    data = serializers.serialize("json", models.Onethink_excellent.objects.filter(id=id))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# CreatePayOrder 党员缴费
@require_POST
def CreatePayOrder(request):
    req = json.loads(request.body)
    id = req.get("id")
    data = serializers.serialize("json", models.Onethink_partycharge.objects.filter(id=id))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)

# 党员缴费
@require_POST
def getPartychargeByid(request):
    req = json.loads(request.body)
    id = req.get("id")
    data = serializers.serialize("json", models.Onethink_partycharge.objects.filter(id=id))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 产品
@require_POST
def getGoodsByCompanyId(request):
    req = json.loads(request.body)
    companyid = req.get("companyid")
    data = serializers.serialize("json", models.Onethink_goods.objects.filter(companyid=companyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 招聘
@require_POST
def getRecruitByCompanyId(request):
    req = json.loads(request.body)
    companyid = req.get("companyid")
    data = serializers.serialize("json", models.Onethink_recruit.objects.filter(companyid=companyid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 评议记录, 字段疑惑 doCommentRecore


# 评议对象 出错
@require_POST
def getCommentobjByCommentd(request):
    req = json.loads(request.body)
    commentid = req.get("commentid")
    data = serializers.serialize("json", models.Onethink_commentobj.objects.filter(commentid=commentid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)


# 志愿者活动 出错
@require_POST
def getVolunteerById(request):
    req = json.loads(request.body)
    id = req.get("id")
    memberid = req.get("memberid")
    data = serializers.serialize("json", models.Onethink_commentobj.objects.filter(id=id, memberid=memberid))
    dict_list = response(data)
    return JsonResponse(dict_list, safe=False)




