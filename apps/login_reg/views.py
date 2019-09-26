from django.shortcuts import render, HttpResponse,redirect
import bcrypt #密码加密
from .models import *
from datetime import date, datetime
from django.contrib import messages

def login(req):
    return render(req, 'login_reg/login.html')

def register(req):
    return render(req,'login_reg/reg.html')

def logging_in(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="login_fail")
        return redirect('/login')
    else:
        user = User.objects.filter(email=request.POST['login_email'])
        logged_user = user[0]
        request.session['user'] = logged_user.first_name
        return redirect('/home')

def reg_form(req):
    errors = User.objects.basic_validator(req.POST)#输入条件限制
    if len(errors) > 0:#输入条件限制
        for key, value in errors.items():#输入条件限制
            messages.error(req, value)#输入条件限制
        return redirect("/login/register")#输入条件限制
    else:
        hashed_pw = bcrypt.hashpw(req.POST['password'].encode(), bcrypt.gensalt())
        user=User.objects.create(first_name = req.POST['firstname'],last_name=req.POST['lastname'],birthday=req.POST['birthday'],email=req.POST['email'],password=hashed_pw)
        req.session['user']=user.first_name
        return redirect("/home")

def main_page(request):
    print('*'*80)
    if 'user' not in request.session:    
        if request.method == "POST":
            request.session['user']=request.POST['login_email']
    return render(request, "home/index.html")

def sign_in_user(request):
    #save user id/name to session
    print(request.POST.getlist('google')[0])
    request.session['user'] = request.POST.getlist('google')[0]
    return redirect('/login/main_page/')

def sign_out(request):
    del request.session['user']
    return redirect('/home/')
