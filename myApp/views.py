from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
import time
import random
from django.http import JsonResponse
import os
from django.contrib.auth import logout
from django.conf import settings

def main(request):
    username = request.session.get('username','未登录')
    usertoken = request.session.get('token')
    MemberRank = request.session.get('MemberRank',' ')
    MemberBlance = request.session.get('MemberBlance', '0')
    MemberIntegral = request.session.get('MemberIntegral', '0')
    loginstatus = request.session.get('loginstatus')
    if loginstatus==True:
        LoginViewstatus = '已登录'
    else:
        LoginViewstatus = '未登录'
    return render(request,'main.html',{'username':username, 'MemberRank':MemberRank,
                                       'MemberBlance':MemberBlance, 'MemberIntegral':MemberIntegral,
                                       'LoginViewstatus': LoginViewstatus})

def regist(request):
   if request.method == 'POST':
        userphone = request.POST.get('userPhone')
        userpasswd = request.POST.get('userPass')
        userrank = '黄金会员'
        userblance = 0
        userintergral = 0
        usercoupon = '无'
        userexpenses_record = '无'
        userloginstatus = False
        usertoken = str(time.time() + random.randrange(1,10000))

        user = User.createuser(userphone, userpasswd,userrank,userblance,
                              userintergral, usercoupon,userexpenses_record,
                               userloginstatus,usertoken )
        user.save()

        request.session['username'] = userphone
        request.session['token'] = usertoken

        return redirect('/membership/main/')
   else:
       return render(request, 'regist.html')


def checkuserid(request):
    userid = request.POST.get('userid')

    try:
        user = User.objects.get(userPhone=userid)
        return JsonResponse({'data': '该用户已被注册', 'status': 'error'})
    except User.DoesNotExist as e:
        return JsonResponse({'data': 'ok', 'status': 'success'})

def quit(request):
    username = request.session.get('username', '登录')
    user = User.objects.get(userPhone=username)
    user.userLoginStatus = False
    logout(request)
    print(user.userLoginStatus)
    return redirect('/membership/main')

from .forms import LoginForm
def login(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():

            nameid = f.cleaned_data['userphone']
            passwd = f.cleaned_data['passwd']

            try:
                user = User.objects.get(userPhone=nameid)
                if user.userpasswd != passwd:
                    return redirect('/membership/login/')
            except user.DoesNotExist as e:
                return redirect('/membership/login/')
            user.userToken = time.time() + random.randrange(1,10000)
            user.userLoginStatus = True
            user.save()

            request.session['username'] = user.userPhone
            request.session['MemberRank'] = user.userRank
            request.session['MemberBlance'] = user.userBlance
            request.session['MemberIntegral'] = user.userIntegral
            request.session['loginstatus'] = user.userLoginStatus
            request.session['token'] = user.userToken
            print(user.userLoginStatus)

            return redirect('/membership/main/')
        else:
            return render(request, 'login.html', {'form': f, 'error':f.errors})
    else:
        f = LoginForm()

    return render(request,'login.html', {'form':f})
