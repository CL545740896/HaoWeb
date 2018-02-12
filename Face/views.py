# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from collections import OrderedDict
from models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import os
import json
import httplib
import urllib
import random


def send_sms(text, mobile):
    host = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 用户名是登录用户中心->验证码短信->产品总览->APIID
    account = "C27266444"
    # 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
    password = "146accbed96f35e016a4b7de6b2e8012"
    params = urllib.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


def getCode():
    code = ''
    s = []
    while (len(s) < 4):
        x = random.randint(0, 9)
        if x not in s:
            s.append(x)
            code = code + str(x)
    return code

def upload_file(request):
    return render(request,'Test.html',locals())
    # if request.method == "POST":    # 请求方法为POST时，进行处理
    #     myFile =request.FILES.get("myfile", None)# 获取上传的文件，如果没有文件，则默认为None
    #     if not myFile:
    #         return HttpResponse("no files for upload!")
    #     destination = open(os.path.join(u"C:/Users/Eric/PycharmProjects/untitled8/static/src/image",'re.jpg'),'wb+') # 打开特定的文件进行二进制的写操作
    #     for chunk in myFile.chunks():      # 分块写入文件
    #         destination.write(chunk)
    #     destination.close()
    #     return render(request, 'upload.html')


def SendMsg(request):
    phone=request.GET.get('phone')
    code=getCode()
    request.session['code']=code
    text = "您的验证码是：" + code + "。请不要把验证码泄露给其他人。"
    print send_sms(text,phone)
    return HttpResponse(u'短信已发送!')

def GetMessage(request):
    if request.method == "POST":
        # file=open(u'客户信息.txt','a+')
        # cardnumber = request.POST.get('cardnumber')
        job_type= request.POST.get('job_type')
        request.session['job_type'] = job_type
        job_address = request.POST.get('job_address')
        request.session['job_address'] =  job_address
        job_age = request.POST.get('job_age')
        if job_age == '' or job_age == None:
            job_age='0'
        if  job_address=='' or job_address==None:
            job_address=u'无工作单位'
        request.session['job_age'] = job_age
        salary_type = request.POST.get('salary_type')
        request.session['salary_type'] = salary_type
        gongjijing_type = request.POST.get('gongjijing_type')
        request.session['gongjijing_type'] = gongjijing_type
        shebao_type = request.POST.get('shebao_type')
        request.session['shebao_type'] = shebao_type
        house_type = request.POST.get('house_type')
        request.session['house_type'] = house_type
        time_shebao = request.POST.get('time_shebao')
        request.session['time_shebao'] = time_shebao
        time_gongjijin = request.POST.get('time_gongjijin')
        request.session['time_gongjijin'] = time_gongjijin
        home_address = request.POST.get('home_address')
        request.session['home_address'] = home_address
        zhimafen= request.POST.get('zhimafen')
        request.session['zhimafen'] =zhimafen
        name=request.session.get('name','')
        money=request.session.get('money','')
        if name=='':
            request.session.clear()
            return HttpResponse(u'非法')
        else:
            # time.sleep(5)
            username = request.session.get('username')
            obj = User.objects.get(username=username)
            obj.home_address=home_address
            obj.job_age=job_age
            obj.job_address=job_address
            obj.name=name
            obj.money=money
            obj.phone=username
            obj.house=house_type
            obj.salary=salary_type
            obj.gongjijing_type=gongjijing_type
            obj.shebao_type=shebao_type
            obj.job_type=job_type
            obj.save()
            return HttpResponse(u'恭喜你初步审核成功!')
        # file.write('****************\n')
        # file.write(u'姓名:'+name+'  '+u'电话:'+phone+' '+u'贷款金额:'+money+'\n')
        # file.write(u'工作地址:' + job_address + '  ' + u'工作年限:' + job_age + '\n ' )
        # # + u'是否代发工资:' + salary + '\n')
        # # file.write(u'公积金:' + gongjijin + '  ' + u'社保:' + shebao + ' ' + u'房子类型:' + livetype + '\n')
        # file.write(u'住址:' + home_address + '  ' + u'芝麻分:' + zhimafen  + '\n')
        # file.write('****************\n\n')
        # file.close()
    else:
        return render(request, 'page2.html')

def  page(request):
    request.session['money'] = request.GET.get('money')
    request.session['name'] = request.GET.get('xm')
    is_alive=request.session.get('password','0')
    print is_alive
    if is_alive !='0':
         return HttpResponse(u'恭喜你初步审核成功!')
    else:
        return HttpResponse(u'请先登录')

def index(request):
    password = request.session.get('password', '')
    return render(request,'index.html',locals())

def user(request):
    name=request.session.get('username','')
    if name=='' or name==None:
        return render(request, 'user.html', locals())
    else:
        Users = User.objects.get(username=name)
        return render(request,'user.html',locals())


def logout(request):
    request.session.clear()
    return render(request,'index.html',locals())

def register(request):
    if request.method=='GET':
     return render(request, 'register.html')
    else:
        code=request.session.get('code','')
        Mycode=request.POST.get('yzm')
        if code==Mycode:
            username=request.POST.get('username')
            password=request.POST.get('password')
            try:
                Myuser = User.objects.get(username=username)
                return HttpResponse(u'该帐号已经注册过了')
            except Exception as e:
                User.objects.create(username=username, password=password)
                request.session['password'] = password
                request.session['username']=username
                return HttpResponse(u'注册成功!')
        else:
            return HttpResponse(u'验证码错误,请重新输入!')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        request.session['username'] = username
        request.session['password'] = password
        print username
        try:
             Myuser= User.objects.get(username=username)
             My_password=Myuser.password
             if My_password==password:
                return HttpResponse(u'登录成功!')
             else:
                 request.session.clear()
                 return HttpResponse(u'密码错误')
        except Exception as e:
             request.session.clear()
             return HttpResponse(u'请先注册后再登录')
    elif request.method=='GET':
        return render(request, 'Login.html')

def result(request):
    name = request.session.get('name', '')
    if name == '' or name==None:
        request.session.clear()
        return render(request, 'index.html')
    else:
        rs=10000
        dic={}
        for keys ,values in  zip(request.session.keys(),request.session.values()):
                dic[keys] = values
        zhimafen=int(dic['zhimafen'])
        if zhimafen<550 or zhimafen>750:
            zhimafen=550
        salary_type=dic['salary_type']
        if salary_type==u'代发':
            salary_type=5000
        else:
            salary_type = 0
        house= dic['house_type']
        if house==u'全款':
            house=100000
        elif house==u'按揭':
            house=50000
        elif house==u'租用':
            house=10000
        time_shebao=dic['time_shebao']
        if time_shebao=='':
            time_shebao=0
        else:
            time_shebao=int(time_shebao)
        time_gongjijin = dic['time_gongjijin']
        if time_gongjijin=='':
            time_gongjijin=0
        else:
            time_gongjijin=int(time_gongjijin)
        rs=rs+(zhimafen-550)*500+(time_gongjijin+time_shebao)*600+house+salary_type

        for key, value in dic.items():
            if value=='':
                 value=u'空'
            print key + ':' + value
        print rs
        username=request.session.get('username')
        obj =User.objects.get(username=username)
        obj.result=rs
        obj.zhimafen=zhimafen
        obj.gongjijintime=time_gongjijin
        obj.shebaotime=time_shebao
        obj.save()
        return render(request, 'Result.html', locals())
def adminLogin(request):
    if request.method=='POST':
        username=request.POST.get('admin')
        password=request.POST.get('password')
        if username=='545740896@qq.com' and password=='159753123':
            UserList = User.objects.order_by('-id')
            paginator = Paginator(UserList, 5)  # Show 25 contacts per page
            page = request.GET.get('page')
            try:
                Users = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                Users = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                Users = paginator.page(paginator.num_pages)
            return render(request, 'Admin.html', locals())
        else:
            return HttpResponse(u'输入错误!')
    else:
         return render(request, 'AdminLogin.html', locals())

def admin(request):
    UserList = User.objects.order_by('-id')
    paginator = Paginator(UserList, 15)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        Users = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        Users = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        Users = paginator.page(paginator.num_pages)
    return render(request, 'Admin.html', locals())

def page_not_found(request):
    return render(request, '404.html',locals())
#
#
# def page_error(request):
#     return render(request, '500.html')
#
#
# def permission_denied(request):
#     return render(request, '403.html')


def danmu(request):
    Color_List=['#20B2AA','#FF0000','#EEEE00','#FF69B4','#00CDCD','#00EE00','#FF4040','#9400D3','#00FF7F']
    if request.method=='POST':
        text = request.POST.get('danmu_text');
        return HttpResponse(u'Success!')
    elif  request.method=='GET':
        text = request.GET.get('text')
        file = open(u'祝福语.txt', 'a+')
        List = []
        while 1:
            lines = file.readlines(100000)
            if not lines:
                break
            for line in lines:
                List.append(line.strip())
        if text!=None:
            img = '/static/src/image/barrager.png'
            text = u'{"img":"' + img + '","info":"' + text + '","color":"#FFFFFF"}'
            file.write(text + '\n')
            return HttpResponse(json.dumps(text), 'content_type="application/json"')
        else:
            danmu_text=random.choice(List)
            color=random.choice(Color_List)
            danmu_text=json.loads(danmu_text,object_pairs_hook=OrderedDict)
            danmu_text["color"]=color
            danmu_text=json.dumps(danmu_text)
            return HttpResponse(json.dumps(danmu_text),'content_type="application/json"')



