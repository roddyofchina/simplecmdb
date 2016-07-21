#coding:utf8
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect,QueryDict
from django.contrib.auth.decorators import login_required
from employeeinfo.models import *
from useraccount.models import User
from django.contrib import auth
from django.contrib.auth.models import Group,Permission
import json
from comm_models.Pagination_set import Page,SearchPage,EmSearchPage
import time
from PIL import Image
from django.conf import settings


@login_required
def employee_list(request,id):
    #用户信息
    userid = request.session.get('user_id')
    username = request.session.get('user_name')
    Userprofile = User.objects.get(id=userid)
    panelsindex, panels1,  panels2 = '首页', '人员管理', '员工管理'


    if request.method == 'GET':
        Employees, pages = Page('/employee/users',id, Employee)
        Depts_Data = Department.objects.all()
        JobTitile = jobtitle.objects.all()
        EmployeeStatus = Employee.u_status
        return render_to_response('employeeinfo/employee.html',locals(),RequestContext(request))
    else:
        searchname= request.POST.get('search')
        if searchname:
            Employees, pages = EmSearchPage('/employee/users',id, Employee, searchname)
            return render_to_response('employeeinfo/employee.html',locals(), RequestContext(request))
        else:
            Employees, pages = Page('/employee/users',id, Employee)
            return render_to_response('employeeinfo/employee.html',locals(), RequestContext(request))


@login_required
def users_query(request):
    if request.method == 'GET':
        search=request.GET['search']
        Employees = Employee.objects.filter(name__contains=search)

        dir_search = []
        for u in Employees:
            data_user={}
            data_user['id']=u.id
            data_user['name']=u.name
        dir_search.append(data_user)
        return HttpResponse(json.dumps(dir_search))




@login_required
def employee_add(request):
    #查询用户信息
    userid = request.session.get('user_id')
    Userprofile = User.objects.get(id=userid)
    if request.method == 'POST':
        if Userprofile.has_perm('employeeinfo.cmdb_employee_add'):
            #添加用户
            name = request.POST.get('name')
            number = request.POST.get('number')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            dept = request.POST.get('dept')
            department = Department.objects.get(id=dept)
            birthday = request.POST.get('birthday')
            sex = request.POST.get('sex')
            entry_time = request.POST.get('entry_time')
            age = request.POST.get('age')
            status = request.POST.get('status')
            Jobtitle_id = request.POST.get('Jobtitle')
            jobtitle_name = jobtitle.objects.get(id=Jobtitle_id)
            universit = request.POST.get('universit')
            family_address = request.POST.get('family_address')
            exitTime = request.POST.get('exitTime')

            if 'photo' in request.FILES:
                image_save_time = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
                image = request.FILES['photo']   #获取前端上传图片
                userimg = Image.open(image)   #打开图片
                userimg.thumbnail((800, 600), Image.ANTIALIAS)  #设置图片比例
                photourl = '/photos/5_' + str(image_save_time) + ".jpg"
                photoname = settings.MEDIA_ROOT + photourl
                userimg.save(photoname, "jpeg")
            else:
                photourl = ''

            p = Employee(name=name, number=number, email=email,sex=sex,\
                    contact=phone, jobtitle=jobtitle_name, dept=department,photo=photourl,age=age,EntryTime=entry_time,\
                    birthday=birthday,status=status,universit=universit,family_address=family_address,ExitTime=exitTime
                    )
            p.save()
            msg={'msginfo':'员工添加成功'}
            return HttpResponse(json.dumps(msg))
        else:
            msg={'msgerror':"该用户没有权限!!!"}
            return HttpResponse(json.dumps(msg))


@login_required
def employee_del(request,uid):
    if request.method == 'GET':
        employee_user = Employee.objects.get(id=uid)
        employee_user.delete()
        msg={'msginfo':"员工信息删除成功"}
        return HttpResponse(json.dumps(msg))
    else:
        datas = request.POST
        Deleteall = json.loads(datas['Checked'])

        for i in Deleteall:
            Employee.objects.get(id=i).delete()

        msg={'msginfo':"批量删除员工成功"}
        return HttpResponse(json.dumps(msg))





@login_required
def JobTitleList(request):
    if request.method == 'GET':
        #用户信息
        userid = request.session.get('user_id')
        username = request.session.get('user_name')
        Userprofile = User.objects.get(id=userid)

        panelsindex, panels1,  panels2 = '首页', '人员管理', '职称管理'

        JobListData = jobtitle.objects.all()

        return render_to_response('employeeinfo/jobtitle.html',locals(),RequestContext(request))



@login_required
def JobTitleAdd(request):
    if request.method == 'POST':
        jobtitle_name = request.POST.get('jobsname')
        exist_name = jobtitle.objects.filter(name=jobtitle_name)
        if exist_name:
            msg={'msgerror':'职称名已存在!!'}
        else:
            jobtitle_add = jobtitle(name=jobtitle_name)
            jobtitle_add.save()
            msg={'msginfo':'职称添加成功!!'}
        return HttpResponse(json.dumps(msg))



@login_required
def JobTitleEdit(request,jobid):
    if request.method == 'GET':
        jobtitle_data = jobtitle.objects.get(id=jobid)
        kdir={
            "jobname": jobtitle_data.name,
            "tag": jobtitle_data.id,
        }
        return HttpResponse(json.dumps(kdir))
    else:
        jobname=request.POST.get('jobname')
        if jobname == "":
            msg={'msgerror':"职称不能为空!!!!"}
        else:
            job_data = jobtitle.objects.get(id=jobid)
            job_data.name = jobname
            job_data.save()
            msg={'msginfo':"职称修改成功!!!"}
        return HttpResponse(json.dumps(msg))


@login_required
def JobTitleDel(request,jobid):
    if request.method == 'GET':
        jobtitle.objects.get(id=jobid).delete()
        msg={'msginfo':"职称删除成功!!!"}
        return HttpResponse(json.dumps(msg))



@login_required
def employee_detail(request, eid):
    if request.method == 'GET':
        pass





@login_required
def employee_edit(request, eid):
    #用户信息
    userid = request.session.get('user_id')
    username = request.session.get('user_name')
    Userprofile = User.objects.get(id=userid)
    panelsindex, panels1,  panels2 = '首页', '人员管理', '人员修改'

    if request.method == 'GET':
        Employee_data = Employee.objects.get(id=eid)
        Department_info = Department.objects.all()
        Employee_status = Employee.u_status
        Department_jobtitle = jobtitle.objects.all()
        return render_to_response('employeeinfo/employee_update.html',locals(),RequestContext(request))
    else:
        if Userprofile.has_perm('employeeinfo.cmdb_employee_change'):
            #添加用户
            name = request.POST.get('name')
            number = request.POST.get('number')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            dept = request.POST.get('dept')
            department = Department.objects.get(id=dept)
            birthday = request.POST.get('birthday')
            sex = request.POST.get('sex')
            entry_time = request.POST.get('entrytime')
            age = request.POST.get('age')
            status = request.POST.get('status')
            Jobtitle_id = request.POST.get('jobtitle')
            jobtitle_name = jobtitle.objects.get(id=Jobtitle_id)
            universit = request.POST.get('universit')
            family_address = request.POST.get('family_address')
            exitTime = request.POST.get('exittime')


            if 'photo' in request.FILES:
                image_save_time = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
                image = request.FILES['photo']   #获取前端上传图片
                userimg = Image.open(image)   #打开图片
                userimg.thumbnail((800, 600), Image.ANTIALIAS)  #设置图片比例
                photourl = '/photos/5_' + str(image_save_time) + ".jpg"
                photoname = settings.MEDIA_ROOT + photourl
                userimg.save(photoname, "jpeg")
            else:
                photourl = ''
            Employee_edit = Employee.objects.get(id=eid)
            Employee_edit.name = name
            Employee_edit.number = number
            Employee_edit.email = email
            Employee_edit.age = age
            Employee_edit.contact = phone
            Employee_edit.dept = department
            Employee_edit.birthday = birthday
            Employee_edit.sex = sex
            Employee_edit.EntryTime = entry_time
            Employee_edit.ExitTime = exitTime
            Employee_edit.status = status
            Employee_edit.jobtitle = jobtitle_name
            Employee_edit.jobtitle = jobtitle_name
            Employee_edit.family_address = family_address
            Employee_edit.family_address = family_address
            Employee_edit.universit = universit
            Employee_edit.save()
            msg={'msginfo':'员工修改成功'}
            return HttpResponse(json.dumps(msg))
        else:
            msg={'msgerror':"该用户没有权限!!!"}
            return HttpResponse(json.dumps(msg))















