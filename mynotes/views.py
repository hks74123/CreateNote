from django.core.checks import messages
from django.shortcuts import redirect, render
from hksnote.models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def show(request):
    hh=mynt.objects.all()
    ll=len(hh)
    return render(request,'done.html', {'hkk':hh,'l':ll})


def notefitback(request):
    ddd=''
    hh=mynt.objects.all()
    ll=len(hh) 
    return render(request,'done.html', {'hkk':hh,'l':ll,'dw':ddd})


def createnote(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        messages.info(request,'Need to login first')
        return render(request,'login.html')


def go(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return render(request,'home.html') 


def notefilt(request):
    if request.user.is_authenticated:
        hh=mynt.objects.filter(tid = request.user)
        ll=len(hh)
        ddd=1
        if hh.exists():
            return render(request,'done.html', {'hkk':hh,'l':ll,'dw':ddd})
        else:
            messages.info(request,"You haven't created a note yet")
            return render(request,'done.html',{'dw':ddd})
    else:
        messages.info(request,'Need to login first')
        return render(request,'login.html')

def createpost(request): 
    if request.method=='POST' and request.user.is_authenticated:
        if request.POST.get('title') and request.POST.get('tags') and request.POST.get('note'):
            pst=mynt()
            pst.tid = request.user
            pst.Title=request.POST.get('title')
            pst.Tag=request.POST.get('tags')
            pst.Note=request.POST.get('note')
            pst.save()
            hh=mynt.objects.all()
            ll=len(hh)
            return render(request,'done.html', {'hkk':hh,'l':ll})
        else:
            return render(request,'index.html')  
    return redirect('/') 

def register(request):
    if request.method=='POST':
        first_name=request.POST['f_name']
        last_name=request.POST['l_name']
        username=request.POST['u_name']
        email=request.POST['mmail']
        passw=request.POST['pass']
        passw1=request.POST['pass1']

        if passw==passw1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exist')
                return redirect('/register')
            else:
                user=User.objects.create_user(username=username, password=passw, email=email, first_name=first_name,last_name=last_name)
                user.save();
                return render(request,'login.html')
        else:
            messages.info(request,'Password not matching')
            return redirect('/register')
        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['ul_name']
        password=request.POST['lpass'] 

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
