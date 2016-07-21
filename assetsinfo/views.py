#coding:utf8
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse, HttpResponseRedirect,QueryDict
from django.contrib.auth.decorators import login_required
from useraccount.models import User
from comm_models.Pagination_set import Page,SearchPage
from comm_models.assets_has_table import tablehas
from comm_models.assets_random import GetAssetsNum

from assetsinfo.models import *
import json


@login_required
def index(request):
    if request.method == 'GET':
        userid=request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)
        panelsindex, panels1,  = '首页', '控制中心',
        return render_to_response('index.html', locals(), RequestContext(request))
@login_required
def assets_list(request,sid):
    if request.method == 'GET':
        userid=request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)
        panelsindex, panels1,  panels2 = '首页', '资产管理', '资产列表'

        AssetsData, pages = Page('/assets/list',sid, Assets)
        return render_to_response('assetsinfo/assets.html',locals(), RequestContext(request))
    else:
        userid=request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)
        panelsindex, panels1,  panels2 = '首页', '资产管理', '资产列表'

        searchname= request.POST.get('search')

        if searchname:
            AssetsData, pages = SearchPage('/assets/list',sid, Assets, searchname)
            return render_to_response('assetsinfo/assets.html',locals(), RequestContext(request))
        else:
            AssetsData, pages = Page('/assets/list',sid, Assets)
            return render_to_response('assetsinfo/assets.html',locals(), RequestContext(request))

@login_required
def assets_add(request):
    userid=request.session.get('user_id')
    username = request.session.get('user_name')
    Userprofile = User.objects.get(id=userid)

    if request.method == 'GET':
        panelsindex, panels1,  panels2 = '首页', '资产管理', '资产添加'
        Provider_data = Provider.objects.all()
        Status_choice = Assets.status_choice
        Buy_type_choice = Assets.buy_type_choice
        assets_type = DeviceType.objects.all()
        AdminUser = User.objects.all()
        Assetsnums = GetAssetsNum()
        Businessdata = Business.objects.all()
        IDCdata = IDC.objects.all()
        return render_to_response('assetsinfo/assets_add.html',locals(), RequestContext(request))
    else:
        assets_name = request.POST.get('assets_name')
        #判断资产名是不是已经存在
        if Assets.objects.filter(Assets_name=assets_name).count() > 0:
            msg={'msgerror':"资产名重复,请重新输入!!!!!"}
            return HttpResponse(json.dumps(msg))

        provider_id = request.POST.get('assets_provider')
        assets_provider = Provider.objects.get(id=provider_id)

        admin_user_id = request.POST.get('admin_users')

        if not admin_user_id:
            admin_users = None
        else:
            admin_users = Employee.objects.get(id=admin_user_id)

        #查询关联设备类型
        typeid = request.POST.get('assets_type')
        assets_type = DeviceType.objects.get(id=typeid)
        assets_price = request.POST.get('assets_price')
        assets_buy_time = request.POST.get('assets_buy_time')
        assets_warranty = request.POST.get('assets_warranty')
        assets_number = request.POST.get('assets_number')
        assets_status = request.POST.get('assets_status')
        assets_buy_type = request.POST.get('assets_buy_type')
        assets_end_time = request.POST.get('assets_end_time')
        assets_use_time = request.POST.get('assets_use_time')

        use_user_id = request.POST.get('use_users')

        if not use_user_id:
            use_users = None
        else:
            use_users = Employee.objects.get(id=use_user_id)

        manager_user = request.POST.get('manager_user')

        #查询关联业务
        businessid = request.POST.get('business')
        business = Business.objects.get(id=businessid)

        #查询关联IDC
        idc_id = request.POST.get('idcinfo')
        idc_info = IDC.objects.get(id=idc_id)
        description = request.POST.get('description')



        Assetsadd = Assets(Assets_name=assets_name,
                           device_number=assets_number,
                           device_type=assets_type,
                           Warranty=assets_warranty,
                           principal=admin_users,
                           Employee=use_users,
                           buy_time=assets_buy_time,
                           buy_type=assets_buy_type,
                           price=assets_price,
                           suse_time=assets_use_time,
                           euse_time=assets_end_time,
                           status=assets_status,
                           description=description,
                           provider=assets_provider,
                           IDC=idc_info,
                           business=business,
                           )
        Assetsadd.save()


        assetid = Assets.objects.get(Assets_name=assets_name)

        for i in json.loads(manager_user):
            User_assets = User.objects.get(id=i)
            assetid.admin.add(User_assets)

        msg={'msginfo':"资产添加成功"}
        return HttpResponse(json.dumps(msg))

@login_required
def assets_del(request,sid):
    if request.method == 'GET':
        #查询用户信息
        userid = request.session.get('user_id')
        Userprofile = User.objects.get(id=userid)

        if Userprofile.has_perm('assetsinfo.cmdb_assets_delete'):
            Assets.objects.get(id=sid).delete()
            msg={'msginfo':"资产删除成功!!!"}
            return HttpResponse(json.dumps(msg))
        else:
            msg={'msgerror':"该用户没有权限!!!"}
            return HttpResponse(json.dumps(msg))
    else:
        datas = request.POST
        Deleteall = json.loads(datas['Checked'])

        for i in Deleteall:
            Assets.objects.get(id=i).delete()

        msg={'msginfo':"批量删除资产成功"}
        return HttpResponse(json.dumps(msg))

@login_required
def assets_details(request,sid):
    if request.method == 'GET':
        userid=request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)

        panelsindex, panels1,  panels2 = '首页', '资产管理', '资产详细'

        details_data = Assets.objects.get(id=sid)
        SelectAdmin= details_data.admin.all()

        return render_to_response('assetsinfo/assets_detail.html',locals(),RequestContext(request))


@login_required
def assets_edit(request,sid):
    if request.method == 'GET':
        userid=request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)

        panelsindex, panels1,  panels2 = '首页', '资产管理', '资产修改'

        Assets_data = Assets.objects.get(id=sid)


        Provider_data = Provider.objects.all()
        Status_choice = Assets.status_choice
        Buy_type_choice = Assets.buy_type_choice
        assets_type = DeviceType.objects.all()
        AdminUser = User.objects.all()
        Assetsnums = GetAssetsNum()
        Businessdata = Business.objects.all()
        IDCdata = IDC.objects.all()
        SelectAdmin= Assets_data.admin.all()
        return render_to_response('assetsinfo/assets_edit.html', locals(), RequestContext(request))


    else:

        assets_name = request.POST.get('assets_name')

        Assets_edit = Assets.objects.get(id=sid)

        #判断资产名是不是已经存在t
        exist_id = Assets.objects.filter(Assets_name=assets_name)
        if exist_id  and  Assets_edit.id != int(sid):
            msg={'msgerror':"资产名重复,请重新输入!!!!!"}
            return HttpResponse(json.dumps(msg))

        provider_id = request.POST.get('assets_provider')
        assets_provider = Provider.objects.get(id=provider_id)
        admin_user_id = request.POST.get('admin_users')
        if not admin_user_id:
            admin_users = None
        else:
            admin_users = Employee.objects.get(id=admin_user_id)

        #查询关联设备类型
        typeid = request.POST.get('assets_type')
        assets_type = DeviceType.objects.get(id=typeid)
        assets_price = request.POST.get('assets_price')
        assets_buy_time = request.POST.get('assets_buy_time')
        assets_warranty = request.POST.get('assets_warranty')
        assets_number = request.POST.get('assets_number')
        assets_status = request.POST.get('assets_status')
        assets_buy_type = request.POST.get('assets_buy_type')
        assets_end_time = request.POST.get('assets_end_time')
        assets_use_time = request.POST.get('assets_use_time')

        use_user_id = request.POST.get('use_users')
        if not use_user_id:
            use_users = None
        else:
            use_users = Employee.objects.get(id=use_user_id)

        manager_user = request.POST.get('manager_user')

        #查询关联业务
        businessid = request.POST.get('business')
        business = Business.objects.get(id=businessid)

        #查询关联IDC
        idc_id = request.POST.get('idcinfo')
        idc_info = IDC.objects.get(id=idc_id)
        description = request.POST.get('description')

        Assets_edit.Asets_name = assets_name
        Assets_edit.device_number = assets_number
        Assets_edit.device_type = assets_type
        Assets_edit.Warranty = assets_warranty
        Assets_edit.principal = admin_users
        Assets_edit.Employee = use_users
        Assets_edit.buy_time = assets_buy_time
        Assets_edit.buy_type = assets_buy_type
        Assets_edit.price = assets_price
        Assets_edit.suse_time = assets_use_time
        Assets_edit.euse_time = assets_end_time
        Assets_edit.status = assets_status
        Assets_edit.description = description
        Assets_edit.provider = assets_provider
        Assets_edit.IDC = idc_info
        Assets_edit.business = business
        Assets_edit.save()
        assetid = Assets.objects.get(id=sid)

        #先删除原来与管理员表（USER）的关联关系
        admins = assetid.admin.all()
        for u in admins:
            assetid.admin.remove(u)

        #重新更新关系表
        for i in json.loads(manager_user):
            User_assets = User.objects.get(id=i)
            assetid.admin.add(User_assets)

        msg={'msginfo':"资产信息修改成功"}
        return HttpResponse(json.dumps(msg))



@login_required
def idc_list(request):
    if request.method == 'GET':
        userid=request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)
        panelsindex, panels1,  panels2 = '首页', '属性设置', 'IDC管理'
        IDCdata = IDC.objects.all()

        return render_to_response('assetsinfo/idcmanager.html',locals(),RequestContext(request))
    else:
        idc_name = request.POST.get('idcname')
        address = request.POST.get('address')
        floor = request.POST.get('floor')
        contacts = request.POST.get('contacts')
        phone = request.POST.get('phone')
        idc_add=IDC(idc_name=idc_name,address=address,floor=floor,contacts=contacts,phone=phone)
        idc_add.save()
        msg={'msginfo':"IDC添加成功!!"}
        return HttpResponse(json.dumps(msg))


@login_required
def idc_edit(request,id):
    if request.method == 'GET':

        IDCdata = IDC.objects.get(id=id)
        kdr={
            'idcname': IDCdata.idc_name,
            'address': IDCdata.address,
            'floor': IDCdata.floor,
            'contacts': IDCdata.contacts,
            'phone': IDCdata.phone,
            'tag': IDCdata.id,
        }
        return HttpResponse(json.dumps(kdr))

    else:
        IDCdata = IDC.objects.get(id=id)
        idc_name = request.POST.get('idcname_edit')
        address = request.POST.get('address_edit')
        floor = request.POST.get('floor_edit')
        contacts = request.POST.get('contacts_edit')
        phone = request.POST.get('phone_number_edit')

        IDCdata.idc_name = idc_name
        IDCdata.address = address
        IDCdata.floor = floor
        IDCdata.contacts = contacts
        IDCdata.phone = phone

        IDCdata.save()

        msg={'msginfo':"IDC修改成功!!"}
        return HttpResponse(json.dumps(msg))









@login_required
def idc_del(request, idcid):
    if request.method == 'GET':
        IDC.objects.get(id=idcid).delete()
        msg={'msginfo':'IDC信息删除成功'}
        return HttpResponse(json.dumps(msg))



@login_required
def business_list(request):
    if request.method == 'GET':
        userid=request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)
        panelsindex, panels1,  panels2 = '首页', '属性设置', '业务管理'
        Business_data = Business.objects.all()

        return render_to_response('assetsinfo/business.html',locals(),RequestContext(request))
    else:
        businessname = request.POST.get('businessname')

        Business_add=Business(name=businessname)
        Business_add.save()
        msg={'msginfo':"业务添加成功!!1"}
        return HttpResponse(json.dumps(msg))


@login_required
def business_del(request):
    if request.method == 'POST':
        pass


@login_required
def business_edit(request,id):
    if request.method == 'GET':
        Business_data = Business.objects.get(id=id)
        kdr ={
            'busname':Business_data.name,
            'tag': Business_data.id,
        }
        return HttpResponse(json.dumps(kdr))

    else:
        busname = request.POST.get('busname')

        Business_data = Business.objects.get(id=id)
        Business_data.name = busname
        Business_data.save()

        msg={'msginfo':"业务修改成功!!"}
        return HttpResponse(json.dumps(msg))


@login_required
def business_del(request,id):
    if request.method == 'GET':
        Business.objects.get(id=id).delete()
        msg={'msginfo':"业务删除成功!!"}
        return HttpResponse(json.dumps(msg))



@login_required
def devicetype_list(request):
    if request.method == 'GET':
        userid=request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)
        panelsindex, panels1,  panels2 = '首页', '属性设置', '设备类型'
        devicetype_data = DeviceType.objects.all()

        return render_to_response('assetsinfo/devicetype.html',locals(),RequestContext(request))
    else:
        type_name = request.POST.get('devicetype_name')
        DeviceType_add=DeviceType(name=type_name)
        DeviceType_add.save()
        msg={'msginfo':"类型添加成功!!"}
        return HttpResponse(json.dumps(msg))




@login_required
def devicetype_edit(request,id):
    if request.method == 'GET':
        DeviceType_data = DeviceType.objects.get(id=id)
        kdr ={
            'typename':DeviceType_data.name,
            'tag': DeviceType_data.id,
        }
        return HttpResponse(json.dumps(kdr))

    else:
        typename = request.POST.get('typename')

        DeviceType_data = DeviceType.objects.get(id=id)
        DeviceType_data.name = typename
        DeviceType_data.save()

        msg={'msginfo':"设备类型修改成功!!"}
        return HttpResponse(json.dumps(msg))





@login_required
def devicetype_del(request,id):
    if request.method == 'GET':
        DeviceType.objects.get(id=id).delete()
        msg={'msginfo':"设备类型删除成功!!"}
        return HttpResponse(json.dumps(msg))




@login_required
def provider_list(request):
    if request.method == 'GET':
        userid=request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)
        panelsindex, panels1,  panels2 = '首页', '属性设置', '提供商管理'
        Provider_data = Provider.objects.all()
        return render_to_response('assetsinfo/providermanager.html',locals(),RequestContext(request))
    else:
        provider_name = request.POST.get('provider_name')
        provider_address = request.POST.get('provider_address')
        provider_contacts = request.POST.get('provider_contacts')
        provider_fax = request.POST.get('provider_fax')
        provider_phone = request.POST.get('provider_phone')

        Provider_add = Provider(provider_name=provider_name,
                              contacts=provider_contacts,
                              address=provider_address,
                              Fax=provider_fax,
                              phone=provider_phone)
        Provider_add.save()

        msg={'msginfo':"提供商添加成功!!!"}
        return HttpResponse(json.dumps(msg))






@login_required
def provider_del(request,id):
    if request.method == 'GET':
        Provider.objects.get(id=id).delete()
        msg = {'msginfo': "提供商删除成功!!!!"}
        return HttpResponse(json.dumps(msg))






@login_required
def provider_edit(request,id):
    if request.method == 'GET':
        Provider_data = Provider.objects.get(id=id)
        kdr = {
            'name': Provider_data.provider_name,
            'address': Provider_data.address,
            'contacts': Provider_data.contacts,
            'phone': Provider_data.phone,
            'Fax': Provider_data.Fax,
            'tag': Provider_data.id,
        }
        return HttpResponse(json.dumps(kdr))

    else:
        Provider_data = Provider.objects.get(id=id)
        Provider_data.provider_name = request.POST.get('provider_name_edit')
        Provider_data.address = request.POST.get('provider_address_edit')
        Provider_data.phone = request.POST.get('provider_phone_edit')
        Provider_data.Fax = request.POST.get('provider_fax_edit')
        Provider_data.contacts = request.POST.get('provider_contacts_edit')

        Provider_data.save()

        msg={'msginfo':"提供商修改成功!!!"}
        return HttpResponse(json.dumps(msg))






@login_required
def Assets_server_list(request):
    if request.method == 'GET':
        userid=request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)
        panelsindex, panels1,  panels2 = '首页', '资源管理', '服务器管理'
        Assets_Server_data = Server.objects.all()

        return render_to_response('assetsinfo/server_list.html',locals(),RequestContext(request))
    else:
        pass





@login_required
def Assets_server_add(request):
    if request.method == 'GET':
        userid=request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)
        panelsindex, panels1,  panels2 = '首页', '资源管理', '服务器添加'
        SoftwareList = Software.objects.all()
        ProviderList  = Provider.objects.all()
        return render_to_response('assetsinfo/server_add.html',locals(),RequestContext(request))
    else:
        pass






@login_required
def Assets_server_edit(request, id):
    if request.method == 'GET':
        pass

    else:
        pass




@login_required
def Assets_server_del(request, id):
    if request.method == 'GET':
        pass
    else:
        pass












