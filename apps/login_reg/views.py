from django.shortcuts import render, HttpResponse,redirect
import bcrypt #密码加密
from .models import *
from datetime import date, datetime
from django.contrib import messages

def login(req):
    return render(req, 'login_reg/login.html')

def register(req):
    return render(req,'login_reg/reg.html')
def login(req):
    users=User.objects.filter(email=req.POST['login_email'])#
    print(f"All users: {users}")
    if len(users) > 0:
        if bcrypt.checkpw(req.POST['login_pw'].encode(), users[0].passoword.encode()):#加密密码确认
            req.session['user'] = users[0].id#加密密码确认
            return redirect("../home")#加密密码确认
    return redirect('/login')

def reg_form(req):
    hashed_pw = bcrypt.hashpw(req.POST['password'].encode(), bcrypt.gensalt())#密码加密

    errors = User.objects.basic_validator(req.POST)#输入条件限制
    if len(errors) > 0:#输入条件限制
        for key, value in errors.items():#输入条件限制
            messages.error(req, value)#输入条件限制
        return redirect("/login/register")#输入条件限制
    else:
        user=User.objects.create(first_name = req.POST['firstname'],last_name=req.POST['lastname'],birthday=req.POST['birthday'],email=req.POST['email'],password=hashed_pw)
        req.session['user']=user.id
        return redirect("/home")