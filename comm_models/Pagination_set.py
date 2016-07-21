#!/usr/bin/env python
#coding:utf-8

__author__ = 'Luodi'
from  django.utils.safestring import mark_safe
from django.db.models import Q


#分页str转成int
def str_int(page):
    try:
        page = int(page)
    except Exception,e:
        page = 1
    return page

'''分页html显示'''


def page_html(page,url,page_counts):
    #显示分页数为11页
    pages_html_list = []



    ul_pages ="""<div ><ul class="pagination">"""
    pages_html_list.append(ul_pages)

    first_html = """<li><a href="%s/%d">首页</a></li>""" %(url,1)
    pages_html_list.append(first_html)
    if page <=1:
        prv_html = """<li class="disabled"><a href="#">上一页</a></li>"""
    else:
        prv_html = """<li><a href="%s/%d">上一页</a></li>""" %(url,page-1)
    pages_html_list.append(prv_html)
    begin_page = page -5
    end = page + 5
    if page_counts <11:
        begin_page = 0
        end = page_counts
    else:
        if page < 6:
            begin_page =0
            end =11
        else:
            if page + 6 > page_counts:
                begin_page = page - 6
                end = page_counts
            else:
                begin_page = page - 6
                end = page + 5

    for i in range(begin_page,end):
        if page == i+1:
            now_page = """<li class="active"><a href="%s/%d">%d</a></li>""" %(url,i+1,i+1)
        else:
            now_page = """<li> <a href="%s/%d">%d</a></li>"""  %(url,i+1,i+1)

        pages_html_list.append(now_page)

    if page+1 > page_counts:
        next_html = """<li class="disabled"><a href="#">下一页<i class="entypo-right-thin"></i></a></li>"""
    else:
        next_html = """<li><a href="%s/%d">下一页<i class="entypo-right-thin"></i></a></li>""" %(url,page+1)

    pages_html_list.append(next_html)


    end_html = """<li><a href="%s/%d">尾页</a></li>""" %(url,page_counts)
    pages_html_list.append(end_html)

    pages_html_list.append("</ul></div>")
    page_result =mark_safe(''.join(pages_html_list))
    return page_result



'''定义分页函数进行分页'''
def Page(geturl,page,tablename):
    page = str_int(page)   #将page转成int
    page_items = 15    #定义每页页数
    start_page = (page - 1) * page_items     #起始数据
    end_page = page * page_items             #截至数据

    count = tablename.objects.all().count()  #获取总数
    resultdata = tablename.objects.all().order_by('-id')[start_page:end_page]   #通过sql的起始数据和截至数据进行查询数据
    temp_resut = divmod(count,page_items)   #是否是分了整页，取余


    if temp_resut[1] == 0:
        page_counts = temp_resut[0]
    else:
        page_counts = temp_resut[0] + 1

    Page_Data= page_html(page,geturl,page_counts)  #     调用html拼接函数
    return resultdata,Page_Data


'''定义分页函数进行分页'''
def SearchPage(geturl,page,tablename,searchname):
    page = str_int(page)   #将page转成int
    page_items = 15    #定义每页页数
    start_page = (page - 1) * page_items     #起始数据
    end_page = page * page_items             #截至数据

    count = tablename.objects.filter(Q(Assets_name__contains=searchname) | Q(device_number__contains=searchname)).count()
    resultdata = tablename.objects.filter(Q(Assets_name__contains=searchname) | Q(device_number__contains=searchname)).order_by('-id')[start_page:end_page]   #通过sql的起始数据和截至数据进行查询数据
    temp_resut = divmod(count,page_items)   #是否是分了整页，取余


    if temp_resut[1] == 0:
        page_counts = temp_resut[0]
    else:
        page_counts = temp_resut[0] + 1

    Page_Data= page_html(page,geturl,page_counts)  #     调用html拼接函数
    return resultdata,Page_Data

'''定义分页函数进行分页'''
def EmSearchPage(geturl,page,tablename,searchname):
    page = str_int(page)   #将page转成int
    page_items = 15    #定义每页页数
    start_page = (page - 1) * page_items     #起始数据
    end_page = page * page_items             #截至数据

    count = tablename.objects.filter(Q(name__contains=searchname) | Q(number__contains=searchname)).count()
    resultdata = tablename.objects.filter(Q(name__contains=searchname) | Q(number__contains=searchname)).order_by('-id')[start_page:end_page]   #通过sql的起始数据和截至数据进行查询数据
    temp_resut = divmod(count,page_items)   #是否是分了整页，取余


    if temp_resut[1] == 0:
        page_counts = temp_resut[0]
    else:
        page_counts = temp_resut[0] + 1

    Page_Data= page_html(page,geturl,page_counts)  #     调用html拼接函数
    return resultdata,Page_Data




