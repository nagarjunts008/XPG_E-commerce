from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from . models import profiles
from django.contrib import messages
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# Create your views here.
def check(email):  
    if(re.search(regex,email)):  
        print("Valid Email") 
        n=1
        return  n
          
    else:  
        print("Invalid Email")
        n=0
        return n



def index(request):
    return render(request,'index.html')

def registers(request):
    if request.method=='POST':
        uname=request.POST['user_name']
        first=request.POST['first_name']
        last=request.POST['last_name']
        emails=request.POST['email']
        dobs=request.POST['dob']
        phoneno=request.POST['phone']
        pwd=request.POST['password']
        cpwd=request.POST['cpassword']

        if pwd==cpwd:
            m=check(emails)
            print(emails)
            if User.objects.filter(username=uname).exists():
                print('User name is taken')
                messages.info(request,'Username is Taken')
                return redirect('/')
            elif User.objects.filter(email=emails).exists():
                print('email is taken')
                messages.info(request,'Email is Taken')
                return redirect('/')
            elif m==0:
                print('Invalid Email')
                messages.info(request,'Invalid Email')
                return redirect('/')
            # elif User.objects.filter(phone=phoneno).exists():
            #     print('Phone number is taken')
            #     messages.info(request,'Phone is Taken')
            #     return redirect('/')
            else:
                user= User.objects.create_user(username=uname, first_name=first, last_name=last, password=pwd, email=emails)
                user.save()
                u = User.objects.get(email=emails)
                p = profiles(date=dobs,phone=phoneno,user_id=u.id)
                p.save()
                
                
                print('successfully user created')
                messages.info(request,'successfully user created')
                return redirect('/')
        else:
            print('password not matching')
            messages.info(request,'password not matching')
            return redirect('/')

        return redirect('/')
    else:
        print('some think went worng')
        return redirect('/')   




def login(request):
    if request.method=='POST':
        uname=request.POST['user_name']
        pwd=request.POST['password']

        user = auth.authenticate(username=uname,password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')
    else:
        return render(request,'/')

