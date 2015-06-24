#-*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils import simplejson
from sysupj.models import Discussion,Student,Course,Teacher,Followings,Material,Rating,Teachings

def home(request):
    username = request.session.get('username')
    if not username:
	    return HttpResponseRedirect('/login/')
    comments = Discussion.objects.order_by('-did').all()
    materials = Material.objects.all()
    username = request.session.get('username')
    return render_to_response("Home.html",{"comments":comments,"username":username,"materials":materials})

def register(request):
    if request.method == "POST":
        sname = request.POST.get('uname','')
        spwd = request.POST.get('pw','')
        if Student.objects.filter(sname=sname):
			return HttpResponse("<html><h1>用户名已存在！</h1></html>")
        s = Student(sname=sname,spwd=spwd)
        s.save()
        return HttpResponse("<html><h1>注册成功！</h1></html>")

def login(request):
    if request.method == "GET":
        return render_to_response("login.html")
    if request.method == "POST":
        sname = request.POST.get('uname','')
        spwd = request.POST.get('pw','')
        student = Student.objects.filter(sname=sname)
        if student:
            if student[0].spwd == spwd:
                request.session['username'] = sname
                return HttpResponseRedirect("/")
        return HttpResponse("<html><h1>用户名或密码有误！</h1></html>")

def logout(request):
    if request.method == "POST":
        del request.session['username']
        return HttpResponseRedirect("/")

def profile(request):
    username = request.session.get('username')
    if username:
        return render_to_response('Home2.html',{"username":username})
    else:
        return HttpResponseRedirect("/login/")

def addComment(request):
    if request.method == "POST":
        username = request.session.get('username')
        if username:
            content = request.POST.get('content','')
            user = Student.objects.get(sname=username)
            d = Discussion(poster=user,dtype=0,target=1,content=content)
            d.save()
            result = {'content':content,'username':username}
        else:
            result = "no login"
        json_result = simplejson.dumps(result,ensure_ascii=False)
        return HttpResponse(json_result,content_type="application/json")

def upload(request):
    username = request.session.get('username')
    if not username:
        return HttpResponseRedirect("/login/")
    if request.method == "POST":
        material = request.FILES['file']
        from os import environ
        online = environ.get("APP_NAME", "")

        if online:
            import sae.const
            access_key = sae.const.ACCESS_KEY  
            secret_key = sae.const.SECRET_KEY
            appname = sae.const.APP_NAME
            domain_name = "pic"

            import sae.storage
            s = sae.storage.Client()
            ob = sae.storage.Object(material.read())
            url = s.put(domain_name, material.name, ob)
            user = Student.objects.get(sname=username)
            course = Course.objects.get(cid=1)
            m = Material(uploader=user,course=course,filepath=url,name=material.name)
            m.save()
            return HttpResponse("<html><h1>上传成功！</h1></html>")

    return HttpResponse("<html><h1>上传失败！</h1></html>")