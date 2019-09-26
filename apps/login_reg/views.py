from django.shortcuts import render, redirect, HttpResponse

def login(req):
    return render(req, 'login_reg/login.html')

def register(req):
    return HttpResponse("haha")