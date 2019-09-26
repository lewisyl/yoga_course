from django.shortcuts import render, redirect, HttpResponse

def login(req):
    return render(req, 'login_reg/login.html')

def register(req):
    return HttpResponse("haha")

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