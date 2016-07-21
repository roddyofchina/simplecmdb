#coding:utf8
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect,QueryDict
from django.contrib.auth.decorators import login_required
from useraccount.models import User,History_Login,Department
from django.contrib import auth
from django.contrib.auth.models import Group,Permission



'''分页模块，传入参数URL,当前页面id，表名'''
from comm_models.Pagination_set import Page
'''用户密码生成模块'''
from django.contrib.auth.hashers import make_password
from django.conf import settings

'''导入图像处理模块'''
from PIL import Image
import time
import json
from useraccount.perm_other import *

addpermission()


def login_user(request):

    if request.method == 'GET':
        return render_to_response('useraccount/login.html', RequestContext(request))

    if request.method == 'POST':

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        #if not request.POST.get('remember_me', None):
        #    request.session.set_expiry(0)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                request.session['user_name'] = user.username
                request.session['user_id'] = user.id
                history_login = History_Login(
                user = user,
                user_ip = request.META['REMOTE_ADDR'],
                )

                history_login.save()

                msg={'accessGranted':"login is ok"}
                return HttpResponse(json.dumps(msg), content_type="application/json")
            else:
                msg={'msgerror':"用户没有激活"}
                return HttpResponse(json.dumps(msg), content_type="application/json")
        else:
            msg={'msgerror':"用户名和密码错误"}
            return HttpResponse(json.dumps(msg), content_type="application/json")



def logout_user(request):
    #记录用户登出时间
    history_login = History_Login.objects.filter(user=request.user).order_by('-id')[0]
    history_login.save()
    #登出用户
    auth.logout(request)
    #删除用户的session
    if request.session.get('user_name'):
        del request.session['user_name']
    return HttpResponseRedirect('/',)


def not_permission(request):
    if request.method == 'GET':
        #用户信息
        userid = request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)
        #导航信息
        panelsindex, panels1, panels2 = '首页', '告警信息','权限告警'

        return  render_to_response('useraccount/not_permission.html',locals(),RequestContext(request))



@login_required
def users_list(request,pgid):
    if request.method == 'GET':

        #用户信息
        userid = request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)

        #权限判断
        if Userprofile.has_perm('useraccount.cmdb_users_view'):
            userid = request.session.get('user_id')
            Rtdata,pages=Page('/users/list',pgid,User)
            #导航信息
            panelsindex, panels1, panels2 = '首页', '用户管理','用户列表'
            Usergroups = Department.objects.all()
            return render_to_response("useraccount/userlist.html", locals(), RequestContext(request))
        else:
            return HttpResponseRedirect('/perm/')



@login_required
def users_add(request):
    #查询用户信息
    userid = request.session.get('user_id')
    Userprofile = User.objects.get(id=userid)
    if request.method == 'POST':
        if Userprofile.has_perm('useraccount.cmdb_users_add'):
            #添加用户
            user_name = request.POST.get('username')
            pass_wd = request.POST.get('passwd')
            email = request.POST.get('email')
            dept = request.POST.get('dept')
            department = Department.objects.get(id=dept)
            phone = request.POST.get('phone')
            realname = request.POST.get('realname')
            is_active = request.POST.get('is_active')
            QQ = request.POST.get('qq_info')

            if 'photo' in request.FILES:
                image_save_time = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
                image = request.FILES['photo']   #获取前端上传图片
                userimg = Image.open(image)   #打开图片
                userimg.thumbnail((128, 128), Image.ANTIALIAS)  #设置图片比例
                photourl = '/photos/119_' + str(image_save_time) + ".jpg"
                photoname = settings.MEDIA_ROOT + photourl
                userimg.save(photoname, "jpeg")
            else:
                photourl = ''

            p = User.objects.create_user(username=user_name, password=pass_wd, email=email,realname=realname,\
                    phone=phone, QQ=QQ, department=department,photo=photourl,)
            p.is_active = is_active
            p.is_staff = True
            p.save()
            msg={'msginfo':'用户添加成功'}
            return HttpResponse(json.dumps(msg))
        else:
            msg={'msgerror':"该用户没有权限!!!"}
            return HttpResponse(json.dumps(msg))


@login_required
def users_update(request,uid):
    #查询用户信息
    username = request.session.get('user_name')
    userid = request.session.get('user_id')
    Userprofile = User.objects.get(id=userid)

    if request.method == 'GET':
        if Userprofile.has_perm('useraccount.cmdb_users_change'):
            Userdata = User.objects.get(id=uid)
            Department_info = Department.objects.all()
            panelsindex, panels1, panels2 = '首页', '用户管理','用户修改'
            return render_to_response("useraccount/userupdate.html",locals(),RequestContext(request))
        else:
            return HttpResponseRedirect('/perm/')

    else:
        UserFile = User.objects.get(id=uid)
        UserFile.username = request.POST.get('username')
        UserFile.email = request.POST.get('email')
        UserFile.realname = request.POST.get('realname')
        UserFile.phone = request.POST.get('phone')
        UserFile.QQ = request.POST.get('qq_info')
        dept_id = request.POST.get('dept')
        dept_name = Department.objects.get(id=dept_id)
        UserFile.department = dept_name
        active = request.POST.get('is_active')
        if int(active) ==1:
            isactive=True
        else:
            isactive=False
        UserFile.is_active = isactive
        if 'photo' in request.FILES:  # 如果用户有上传头像就更新，否则不更新
            image_save_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
            image = request.FILES['photo']  # 获取前端上传图片
            userimg = Image.open(image)  # 打开图片
            userimg.thumbnail((128, 128), Image.ANTIALIAS)  # 设置图片比例
            photourl = '/photos/119_' + str(image_save_time) + ".jpg"
            photoname = settings.MEDIA_ROOT + photourl
            userimg.save(photoname, "jpeg")
            UserFile.photo = photourl

        UserFile.save()
        #修改成功返回消息
        msg={'msginfo':'用户信息修改成功'}
        return HttpResponse(json.dumps(msg))


@login_required
def users_del(request, uid):
    if request.method == 'GET':
        #查询用户信息
        userid = request.session.get('user_id')
        Userprofile = User.objects.get(id=userid)
        if Userprofile.has_perm('useraccount.cmdb_users_delete'):
            User.objects.get(id=uid).delete()
            msg={'msginfo':"用户删除成功!!!"}
            return HttpResponse(json.dumps(msg))
        else:
            msg={'msgerror':"该用户没有权限!!!"}
            return HttpResponse(json.dumps(msg))



@login_required
def userset_password(request, uid):

    #查询用户信息
    username = request.session.get('user_name')
    userid = request.session.get('user_id')
    Userprofile = User.objects.get(id=userid)

    '''当前用户可以修改自已密码，如果赋予修改密码权限即可以修改其它用户的密码，一般建议赋予超级管理员'''
    if request.method == 'GET':
        uid = uid
        if int(uid) == userid:
            panelsindex, panels1, panels2 = '首页', '用户管理','密码重置'
            return render_to_response("useraccount/password_set.html",locals(),RequestContext(request))
        else:
            if Userprofile.has_perm('useraccount.cmdb_users_restpass'):
                panelsindex, panels1, panels2 = '首页', '用户管理','密码重置'
                return render_to_response("useraccount/password_set.html",locals(),RequestContext(request))
            else:
                return HttpResponseRedirect('/perm/')


    if request.method == 'POST':
        Userdata = User.objects.get(id=uid)
        firstpasswd = request.POST.get('firstpasswd')
        secondpasswd = request.POST.get('secondpasswd')
        if firstpasswd == secondpasswd:
            Userdata.set_password(firstpasswd)
            Userdata.save()
            msg={'msginfo':'修改密码成功'}
            return HttpResponse(json.dumps(msg))
        else:
            msg={'msgerror':'两次密码输入不一致'}
            return HttpResponse(json.dumps(msg))



@login_required
def users_info(request, uid):
    if request.method == 'GET':
        Userinfo = User.objects.get(id=uid)

        #查询用户信息
        username = request.session.get('user_name')
        userid = request.session.get('user_id')
        Userprofile = User.objects.get(id=userid)
        panelsindex, panels1, panels2 = '首页', '用户管理','用户详细信息'

        return render_to_response("useraccount/userinfo.html",locals(), RequestContext(request))




@login_required
def users_group_list(request, gid):
    if request.method == 'GET':
        Groupdata, pages = Page('/users/groups/list',gid, Group)
        GroupUserCount = Group.objects.all()
        #查询用户信息
        username = request.session.get('user_name')
        userid = request.session.get('user_id')
        Userprofile = User.objects.get(id=userid)

        panelsindex, panels1, panels2 = '首页', '用户组管理','用户组列表'


        Gdirs={}
        for g in GroupUserCount:
            Ucount = g.user_set.count()
            Gdirs[g.name] = Ucount

        return  render_to_response("useraccount/groupslist.html",locals(),RequestContext(request))



@login_required
def users_group_add(request):
    #查询用户信息
    userid = request.session.get('user_id')
    Userprofile = User.objects.get(id=userid)

    if request.method == 'POST':
        if Userprofile.has_perm('auth.cmdb_group_add'):
            groupname = request.POST.get('groupname')
            if groupname == "":
                msg={'msgerror':"组名不能为空!!!"}
            else:
                gsave=Group(name=groupname)
                gsave.save()
                msg={'msginfo':"用户组添加成功!!!"}
            return HttpResponse(json.dumps(msg))
        else:
            msg={'msgerror':"该用户没有权限!!!"}
            return HttpResponse(json.dumps(msg))



@login_required
def users_group_edit(request, gid):

    #查询用户信息
    userid = request.session.get('user_id')
    Userprofile = User.objects.get(id=userid)

    if request.method == 'GET':
        if Userprofile.has_perm('auth.cmdb_group_change'):
            group_data = Group.objects.get(id=gid)
            kdir={
                "groupname": group_data.name,
                "tag": group_data.id,
            }
            return HttpResponse(json.dumps(kdir))
        else:
            msg={'msgerror':'该用户没有权限!!!'}
            return HttpResponse(json.dumps(msg))
    else:
        if Userprofile.has_perm('auth.cmdb_group_change'):
            gname=request.POST.get('groupname')
            group_data = Group.objects.get(id=gid)
            group_data.name = gname
            group_data.save()
            msg={'msginfo':"用户组修改成功!!!"}
            return HttpResponse(json.dumps(msg))
        else:
            msg={'msgerror':"该用户没有权限!!!"}
            return HttpResponse(json.dumps(msg))




@login_required
def users_group_del(request, gid):
    if request.method == 'GET':

        #查询用户信息
        username = request.session.get('user_name')
        userid = request.session.get('user_id')
        Userprofile = User.objects.get(id=userid)

        if Userprofile.has_perm("auth.cmdb_group_delete"):
            Group_data = Group.objects.get(id=gid)
            if Group_data.user_set.count() == 0 and Group_data.permissions.count() == 0:
                Group_data.delete()

                msg={'msginfo':"用户组删除成功!!!"}
                return HttpResponse(json.dumps(msg))
            else:
                msg={'msgerror':"请移除该组中的用户或权限!!!"}
                return HttpResponse(json.dumps(msg))
        else:
            msg={'msgerror':"该用户没有权限!!!"}
            return HttpResponse(json.dumps(msg))




@login_required
def users_group_manager(request,groupid):
    groupid = groupid

    #查询用户信息
    username = request.session.get('user_name')
    userid = request.session.get('user_id')
    Userprofile = User.objects.get(id=userid)

    if request.method == 'GET':
        if Userprofile.has_perm('auth.cmdb_group_change'):
            Group_data = Group.objects.get(id=groupid)
            #反查组包含的用户
            Guserdata = Group_data.user_set.all()
            Usersdata = User.objects.all()

            #先获取所有用户关联组的信息
            User_in_groups = {}
            for line in Guserdata:
                User_in_groups[line.username] = line.id

            #匹配没有关联组的用户信息key:value
            User_notin_groups={}
            for u in Usersdata:
                if not u.username in User_in_groups.keys():
                    User_notin_groups[u.username] = u.id

            #导航信息栏
            panelsindex, panels1, panels2 = '首页', '用户组管理','成员管理'
            return render_to_response("useraccount/groupsmanager.html",locals(),RequestContext(request))
        else:
            return HttpResponseRedirect('/perm/')
    else:
        getdata = request.POST
        from_Data = json.loads(getdata['from'])
        to_data = json.loads(getdata['to'])

        if from_Data:
            for line in from_Data:
                user_get = User.objects.get(username=line['name'])
                group_get = Group.objects.get(id=groupid)
                user_get.groups.add(group_get)

        if to_data:
            for toline in to_data:
                user_get = User.objects.get(username=toline['name'])
                groupto_get = Group.objects.get(id=groupid)
                user_get.groups.remove(groupto_get)

        msg={'msginfo':"组成员信息已更新!!!"}
        return HttpResponse(json.dumps(msg))





@login_required
def users_history(request, pgid):
    if request.method  == 'GET':
        Rtdata,pages=Page('/users/history',pgid,History_Login)

        #查询用户信息
        username = request.session.get('user_name')
        userid = request.session.get('user_id')
        Userprofile = User.objects.get(id=userid)

        #权限判断
        if Userprofile.has_perm('useraccount.cmdb_history_view'):
            panelsindex, panels1, panels2 = '首页', '登录历史','登录历史列表'

            return render_to_response("useraccount/login_history.html", locals(), RequestContext(request))
        else:
            return HttpResponseRedirect('/perm/')



@login_required
def users_history_del(request, hid):
    if request.method == 'GET':
        userid = request.session.get('user_id')
        Userprofile = User.objects.get(id=userid)

        if Userprofile.has_perm('useraccount.cmdb_history_delete'):
            History_Login.objects.get(id=hid).delete()
            msg={'msginfo':"删除成功!!!"}
            return HttpResponse(json.dumps(msg))
        else:
            msg={'msgerror':"该用户没有权限!!!"}
            return HttpResponse(json.dumps(msg))




@login_required
def User_permissions(request, gid):
    if request.method == 'GET':
        #查询用户信息
        username = request.session.get('user_name')
        userid = request.session.get('user_id')
        Userprofile = User.objects.get(id=userid)

        if Userprofile.has_perm('auth.cmdb_permission_view'):
            Perdata, pages = Page('/groups/list',gid,Group)
            GroupperCount = Group.objects.all()
            panelsindex, panels1, panels2 = '首页', '权限管理','用户组权限列表'

            return  render_to_response("useraccount/permission_list.html",locals(),RequestContext(request))
        else:
            return HttpResponseRedirect('/perm/')



@login_required
def users_permission_managers(request,groupid):
    groupid=groupid
    if request.method == 'GET':
        #查询用户信息
        username = request.session.get('user_name')
        userid = request.session.get('user_id')
        Userprofile = User.objects.get(id=userid)

        if Userprofile.has_perm('auth.cmdb_permission_change'):
            Group_permissons = Group.objects.get(id=groupid)
            Selected = Group_permissons.permissions.all()

            Permission_data = Permission.objects.filter(codename__contains="cmdb")

            #匹配在用户组的权限
            Permission_in_Groups = {}
            for p_in in Selected:
                Permission_in_Groups[p_in.id] = p_in.name


            #匹配没有关联组的权限信息key:value
            Permission_notin_groups = {}
            for p in Permission_data:
                if not p.id in Permission_in_Groups.keys():
                    Permission_notin_groups[p.id] = p.name


            return render_to_response('useraccount/permissionmanager.html',locals(),RequestContext(request))
        else:
            return HttpResponseRedirect('/perm/')

    else:
        getdata = request.POST
        from_Data = json.loads(getdata['from'])
        to_data = json.loads(getdata['to'])

        '''实现逻辑 后台获取选择的权限，或取消的权限。1.查询选择的所有权，添加到组。取消也是如此'''

        if from_Data:
            for line in from_Data:

                permission_get = Permission.objects.get(id=line['value'])
                group_get = Group.objects.get(id=groupid)
                group_get.permissions.add(permission_get)

        if to_data:
            for toline in to_data:

                permission_get = Permission.objects.get(id=toline['value'])
                group_get = Group.objects.get(id=groupid)
                group_get.permissions.remove(permission_get)

        msg={'msginfo':"组权限信息已更新!!!"}
        return HttpResponse(json.dumps(msg))



@login_required
def dept_lists(request,did):

    if request.method == 'GET':
        #查询用户信息
        username = request.session.get('user_name')
        userid = request.session.get('user_id')
        Userprofile = User.objects.get(id=userid)
        if Userprofile.has_perm('useraccount.cmdb_dept_view'):
            Deptdata, pages = Page('/users/dept/list',did,Department)
            panelsindex, panels1, panels2 = '首页', '部门管理','部门列表'

            return render_to_response('useraccount/deptlist.html',locals(),RequestContext(request))
        else:
            return HttpResponseRedirect('/perm/')


@login_required
def dept_del(request,did):
    if request.method == 'GET':
        #查询用户信息
        userid = request.session.get('user_id')
        Userprofile = User.objects.get(id=userid)

        if Userprofile.has_perm('useraccount.cmdb_dept_delete'):
            Dept_Userall = Department.objects.get(id=did)
            if Dept_Userall.user_set.count() == 0:
                Department.objects.get(id=did).delete()
                msg={'msginfo':"部门删除成功!!!"}
                return HttpResponse(json.dumps(msg))
            else:
                msg={'msgerror':"请删除关联用户!!!"}
                return HttpResponse(json.dumps(msg))
        else:
            msg={'msgerror':"该用户没有权限!!!"}
            return HttpResponse(json.dumps(msg))




@login_required
def dept_add(request):
    #查询用户信息
    userid = request.session.get('user_id')
    Userprofile = User.objects.get(id=userid)

    if request.method == 'POST':
        if Userprofile.has_perm('useraccount.cmdb_dept_add'):
            deptname = request.POST.get('deptname')
            dsave=Department(name=deptname)
            dsave.save()
            msg={'msginfo':"部门添加成功!!!"}
            return HttpResponse(json.dumps(msg))
        else:
            msg={'msgerror':"该用户没有权限!!!"}
            return HttpResponse(json.dumps(msg))


@login_required
def dept_edit(request,did):
    #查询用户信息
    userid = request.session.get('user_id')
    Userprofile = User.objects.get(id=userid)

    if request.method == 'GET':
        if Userprofile.has_perm('useraccount.cmdb_dept_change'):
            dept_data = Department.objects.get(id=did)
            kdir={
                "deptname": dept_data.name,
                "tag": dept_data.id,
            }
            return HttpResponse(json.dumps(kdir))
        else:
            msg={"msgerror":"该用户没有权限!!!"}
            return HttpResponse(json.dumps(msg))
    else:
        dname=request.POST.get('deptname')
        if dname == "":
            msg={'msgerror':"部门不能为空!!!!"}
        else:
            dept_data = Department.objects.get(id=did)
            dept_data.name = dname
            dept_data.save()
            msg={'msginfo':"部门修改成功!!!"}
        return HttpResponse(json.dumps(msg))

















