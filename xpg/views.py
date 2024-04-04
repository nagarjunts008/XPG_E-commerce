from django.shortcuts import render,redirect, HttpResponse
from . models import ecmodel,csmodel,memodel,eemodel,tcmodel,melmodel,xprojectmodel,othermodel,developermodel,cartmodel,buyer,reviewmodel
from accounts.models import profiles
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
import json



# Create your views here.
def BootstrapFilterView(request):
    return render(request, "bootstrapfilter.html", {})

def base(request):
    return render(request,'base.html')

def maps(request):
    return render(request,'maps.html')

def home(request):
    x={"csprods":csmodel.objects.all(), "ecprods":ecmodel.objects.all(),"eeprods":eemodel.objects.all(),"meprods":memodel.objects.all(),"tcprods":tcmodel.objects.all(),"melprods":melmodel.objects.all()}
    return render(request,'home.html',{'mixprods':x})

def xproject(request):
    prods=xprojectmodel.objects.all()
    return render(request,'xproject.html',{'prods':prods})

def ec(request):
    prods=ecmodel.objects.all()
    return render(request,'ec.html',{'prods':prods})

def cs(request):
    prods=csmodel.objects.all()
    return render(request,'cs.html',{'prods':prods})

def me(request):
    prods=memodel.objects.all()
    return render(request,'me.html',{'prods':prods})

def ee(request):
    prods=eemodel.objects.all()
    return render(request,'ee.html',{'prods':prods})

def tc(request):
    prods=tcmodel.objects.all()
    return render(request,'tc.html',{'prods':prods})

def mel(request):
    prods=melmodel.objects.all()
    return render(request,'mel.html',{'prods':prods})

def other(request):
    prods=othermodel.objects.all()
    return render(request,'other.html',{'prods':prods})


def cart(request,user):
    user=User.objects.get(username=user)
    cartlists=cartmodel.objects.filter(uid=user.id)
    #cartlists=cartmodel.objects.get(uid=user.id)
    return render(request,'cart.html',{'cart':cartlists})


def cart_delete(request,user,product,id):
    cartdelete=cartmodel.objects.get(id=id)
    cartdelete.delete()
    print('successfully Product removed from cart')
    messages.info(request,'successfully Product removed from cart')
    print("<===================>")
    return redirect('home')

def order_delete(request,user,product,id):
    orderdelete=buyer.objects.get(id=id)
    orderdelete.delete()
    print('successfully Product removed from ordered Placed')
    messages.info(request,'successfully Product removed from ordered Placed')
    print("<===================>")
    return redirect('home')


def order(request,user):
    user=User.objects.get(username=user)
    orderlists=buyer.objects.filter(uid=user.id)
    return render(request,'order.html',{'order':orderlists})

def address(request,user,product,id):
    print(id)
    cartlists=cartmodel.objects.filter(id=id)
    return render(request,'address.html',{'carts':cartlists})
    
def pyfoo(request) : 
    try:
        print("<===================>")
        global latitude, longitude 
        latitude = request.GET['latitude']
        longitude = request.GET['longitude']
        print("latitude=",latitude,"logitude=",longitude)
        print("<===================>")
        return HttpResponse("Done")
    except ValueError:
        return HttpResponse("Failed")



def buy(request,user,id):
    print(latitude, longitude)
    if request.method=='POST':
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        city=request.POST.get('city')
        state=request.POST.get('state')
        postcode=request.POST.get('postcode')
        country=request.POST.get('country')
        
        img=request.POST.get('productimg')
        pid=request.POST.get('productid')
        productname=request.POST.get('productname')
        desc=request.POST.get('productdesc')
        price=request.POST.get('productprice')
        pcat=request.POST.get('pcategory')

        print("<===================>")
        print("Username=",user,"\nuid=",id,"\npname=",productname,"\npid=",pid,"\nimg=",img,"\nprice=",price,"\ndesc=",desc)
        print("\naddress1=",address1,"\naddress2=",address2,"\ncity=",city,"\nstate=",state,"\npostcode=",postcode,"\ncountry=",country)
        buy= buyer(username=user, uid=id, pname=productname, pid=pid, img=img, price=price, desc=desc, address1=address1, address2=address2, city=city, state=state, postcode=postcode, country=country, pcategory=pcat, latitude=latitude, longitude=longitude)
        buy.save()
        print('successfully added to buy')
        messages.info(request,'successfully added to buy')
        print("<===================>")
        print(latitude, longitude)
        cartlists=cartmodel.objects.filter(id=pid)
        cartlists.delete()
        return redirect('home')


def add_to_card(request,user,product,id):
    user=User.objects.get(username=user)
    print("<===================>")
    text=str(product)
    rest = text.split()
    modelname=rest[0]
    print(modelname,id)
    print(eval(modelname))
    cart= eval(modelname).objects.get(id=id)
    productname=cart.name
    price=cart.price
    desc=cart.desc
    img=cart.img
    pcat=cart.category
    print("\n\n Username=",user,"\npname=",productname,"\nprice=",price,"\ndesc=",desc,"\nimg=",img,"\nuid",user.id,"\npcategory=",pcat)

    newcart= cartmodel(username=user, productname=productname, price=price, desc=desc, img=img, uid=user.id, pcategory=pcat)
    newcart.save()
    print('successfully Product added to cart')
    messages.info(request,'successfully Product added to cart')
    print("<===================>")
    return redirect('home')




def about(request):
    return render(request,'about.html')

def help(request):
    return render(request,'help.html')

def developer(request):
    dmembers=developermodel.objects.all()
    return render(request,'services.html',{'dmembers':dmembers})

def new_reviews(request,product,pid,user,id):
    text=str(product)
    rest = text.split()
    modelname=rest[0]
    star=request.POST.get('starstyle')
    print(star)
    title=request.POST.get('review_title')
    new_review=request.POST.get('new_review')
    reviews= reviewmodel(department=modelname, pid=pid, user=user, uid=id, title=title, review=new_review, star=int(star))
    reviews.save()
    print('successfully Review is added')
    messages.info(request,'successfully Review is added')
    print("<===================>")
    return redirect('home')

def ec_details_show(request,id):
    product=ecmodel.objects.get(id=id)
    reviews=reviewmodel.objects.filter(pid=id,department='ecmodel')
    print("<===============================>")
    a=[]
    t=0
    s5=0
    s4=0
    s3=0
    s2=0
    s1=0
    for n in range(len(reviews)):
        for i in  range(reviews[n].star):
            a.append(i)
        t=t+a[-1]+1
        if 5 == a[-1]+1:
            s5=s5+1
        elif 4 == a[-1]+1:
            s4=s4+1
        elif 3 == a[-1]+1:
            s3=s3+1
        elif 2 == a[-1]+1:
            s2=s2+1
        else:
            s1=s1+1
    if t != 0:
        avg=((t)/(len(reviews)*5))*100

        print(s5,s4,s3,s2,s1)
        avg5=(s5/len(reviews))*100
        avg4=(s4/len(reviews))*100
        avg3=(s3/len(reviews))*100
        avg2=(s2/len(reviews))*100
        avg1=(s1/len(reviews))*100
    else:
        avg=0
        avg5=0
        avg4=0
        avg3=0
        avg2=0
        avg1=0

    print(avg,avg5,avg4,avg3,avg2,avg1)
    totalrater=len(reviews)
    print("totalrater",avg)
    totalstar=((((avg)/2))/10)
    print("totalstar",totalstar)
    print("<===============================>")
    z=[]
    ss=round(totalstar)
    for i in range(ss):
        z.append(i)
    print(z)
    x={"product":product, "reviews":reviews,"avg":int(avg),"totalstar":round(totalstar,1),"avg5":avg5,"avg4":avg4,"avg3":avg3,"avg2":avg2,"avg1":avg1,"totalrater":totalrater,"intstar":z}
    return render(request,'details.html',{'x':x})   

def cs_details_show(request,id):
    product=csmodel.objects.get(id=id)
    reviews=reviewmodel.objects.filter(pid=id,department='csmodel')
    print("<===============================>")
    a=[]
    t=0
    s5=0
    s4=0
    s3=0
    s2=0
    s1=0
    for n in range(len(reviews)):
        for i in  range(reviews[n].star):
            a.append(i)
        t=t+a[-1]+1
        if 5 == a[-1]+1:
            s5=s5+1
        elif 4 == a[-1]+1:
            s4=s4+1
        elif 3 == a[-1]+1:
            s3=s3+1
        elif 2 == a[-1]+1:
            s2=s2+1
        else:
            s1=s1+1
    if t != 0:
        avg=((t)/(len(reviews)*5))*100

        print(s5,s4,s3,s2,s1)
        avg5=(s5/len(reviews))*100
        avg4=(s4/len(reviews))*100
        avg3=(s3/len(reviews))*100
        avg2=(s2/len(reviews))*100
        avg1=(s1/len(reviews))*100
    else:
        avg=0
        avg5=0
        avg4=0
        avg3=0
        avg2=0
        avg1=0

    print(avg,avg5,avg4,avg3,avg2,avg1)
    totalrater=len(reviews)
    print("totalrater",avg)
    totalstar=((((avg)/2))/10)
    print("totalstar",round(totalstar,1))
    z=[]
    ss=round(totalstar)
    for i in range(ss):
        z.append(i)
    print(z)
    x={"product":product, "reviews":reviews,"avg":int(avg),"totalstar":round(totalstar,1),"avg5":avg5,"avg4":avg4,"avg3":avg3,"avg2":avg2,"avg1":avg1,"totalrater":totalrater,"intstar":z}
    return render(request,'details.html',{'x':x})  
   

def ee_details_show(request,id):
    product=eemodel.objects.get(id=id)
    reviews=reviewmodel.objects.filter(pid=id,department='eemodel')
    print("<===============================>")
    a=[]
    t=0
    s5=0
    s4=0
    s3=0
    s2=0
    s1=0
    for n in range(len(reviews)):
        for i in  range(reviews[n].star):
            a.append(i)
        t=t+a[-1]+1
        if 5 == a[-1]+1:
            s5=s5+1
        elif 4 == a[-1]+1:
            s4=s4+1
        elif 3 == a[-1]+1:
            s3=s3+1
        elif 2 == a[-1]+1:
            s2=s2+1
        else:
            s1=s1+1
    if t != 0:
        avg=((t)/(len(reviews)*5))*100

        print(s5,s4,s3,s2,s1)
        avg5=(s5/len(reviews))*100
        avg4=(s4/len(reviews))*100
        avg3=(s3/len(reviews))*100
        avg2=(s2/len(reviews))*100
        avg1=(s1/len(reviews))*100
    else:
        avg=0
        avg5=0
        avg4=0
        avg3=0
        avg2=0
        avg1=0

    print(avg,avg5,avg4,avg3,avg2,avg1)
    totalrater=len(reviews)
    print("totalrater",avg)
    totalstar=((((avg)/2))/10)
    print("totalstar",totalstar)
    print("<===============================>")
    z=[]
    ss=round(totalstar)
    for i in range(ss):
        z.append(i)
    print(z)
    x={"product":product, "reviews":reviews,"avg":int(avg),"totalstar":round(totalstar,1),"avg5":avg5,"avg4":avg4,"avg3":avg3,"avg2":avg2,"avg1":avg1,"totalrater":totalrater,"intstar":z}
    return render(request,'details.html',{'x':x})  

def tc_details_show(request,id):
    product=tcmodel.objects.get(id=id)
    reviews=reviewmodel.objects.filter(pid=id,department='tcmodel')
    print("<===============================>")
    a=[]
    t=0
    s5=0
    s4=0
    s3=0
    s2=0
    s1=0
    for n in range(len(reviews)):
        for i in  range(reviews[n].star):
            a.append(i)
        t=t+a[-1]+1
        if 5 == a[-1]+1:
            s5=s5+1
        elif 4 == a[-1]+1:
            s4=s4+1
        elif 3 == a[-1]+1:
            s3=s3+1
        elif 2 == a[-1]+1:
            s2=s2+1
        else:
            s1=s1+1
    if t != 0:
        avg=((t)/(len(reviews)*5))*100

        print(s5,s4,s3,s2,s1)
        avg5=(s5/len(reviews))*100
        avg4=(s4/len(reviews))*100
        avg3=(s3/len(reviews))*100
        avg2=(s2/len(reviews))*100
        avg1=(s1/len(reviews))*100
    else:
        avg=0
        avg5=0
        avg4=0
        avg3=0
        avg2=0
        avg1=0

    print(avg,avg5,avg4,avg3,avg2,avg1)
    totalrater=len(reviews)
    print("totalrater",avg)
    totalstar=((((avg)/2))/10)
    print("totalstar",totalstar)
    print("<===============================>")
    z=[]
    ss=round(totalstar)
    for i in range(ss):
        z.append(i)
    print(z)
    x={"product":product, "reviews":reviews,"avg":int(avg),"totalstar":round(totalstar,1),"avg5":avg5,"avg4":avg4,"avg3":avg3,"avg2":avg2,"avg1":avg1,"totalrater":totalrater,"intstar":z}
    return render(request,'details.html',{'x':x})  

def me_details_show(request,id):
    product=memodel.objects.get(id=id)
    reviews=reviewmodel.objects.filter(pid=id,department='memodel')
    print("<===============================>")
    a=[]
    t=0
    s5=0
    s4=0
    s3=0
    s2=0
    s1=0
    for n in range(len(reviews)):
        for i in  range(reviews[n].star):
            a.append(i)
        t=t+a[-1]+1
        if 5 == a[-1]+1:
            s5=s5+1
        elif 4 == a[-1]+1:
            s4=s4+1
        elif 3 == a[-1]+1:
            s3=s3+1
        elif 2 == a[-1]+1:
            s2=s2+1
        else:
            s1=s1+1
    if t != 0:
        avg=((t)/(len(reviews)*5))*100

        print(s5,s4,s3,s2,s1)
        avg5=(s5/len(reviews))*100
        avg4=(s4/len(reviews))*100
        avg3=(s3/len(reviews))*100
        avg2=(s2/len(reviews))*100
        avg1=(s1/len(reviews))*100
    else:
        avg=0
        avg5=0
        avg4=0
        avg3=0
        avg2=0
        avg1=0

    print(avg,avg5,avg4,avg3,avg2,avg1)
    totalrater=len(reviews)
    print("totalrater",avg)
    totalstar=((((avg)/2))/10)
    print("totalstar",totalstar)
    print("<===============================>")
    z=[]
    ss=round(totalstar)
    for i in range(ss):
        z.append(i)
    print(z)
    x={"product":product, "reviews":reviews,"avg":int(avg),"totalstar":round(totalstar,1),"avg5":avg5,"avg4":avg4,"avg3":avg3,"avg2":avg2,"avg1":avg1,"totalrater":totalrater,"intstar":z}
    return render(request,'details.html',{'x':x})  
def mel_details_show(request,id):
    product=melmodel.objects.get(id=id)
    reviews=reviewmodel.objects.filter(pid=id,department='melmodel')
    print("<===============================>")
    a=[]
    t=0
    s5=0
    s4=0
    s3=0
    s2=0
    s1=0
    for n in range(len(reviews)):
        for i in  range(reviews[n].star):
            a.append(i)
        t=t+a[-1]+1
        if 5 == a[-1]+1:
            s5=s5+1
        elif 4 == a[-1]+1:
            s4=s4+1
        elif 3 == a[-1]+1:
            s3=s3+1
        elif 2 == a[-1]+1:
            s2=s2+1
        else:
            s1=s1+1
    if t != 0:
        avg=((t)/(len(reviews)*5))*100

        print(s5,s4,s3,s2,s1)
        avg5=(s5/len(reviews))*100
        avg4=(s4/len(reviews))*100
        avg3=(s3/len(reviews))*100
        avg2=(s2/len(reviews))*100
        avg1=(s1/len(reviews))*100
    else:
        avg=0
        avg5=0
        avg4=0
        avg3=0
        avg2=0
        avg1=0

    print(avg,avg5,avg4,avg3,avg2,avg1)
    totalrater=len(reviews)
    print("totalrater",avg)
    totalstar=((((avg)/2))/10)
    print("totalstar",totalstar)
    print("<===============================>")
    z=[]
    ss=round(totalstar)
    for i in range(ss):
        z.append(i)
    print(z)
    x={"product":product, "reviews":reviews,"avg":int(avg),"totalstar":round(totalstar,1),"avg5":avg5,"avg4":avg4,"avg3":avg3,"avg2":avg2,"avg1":avg1,"totalrater":totalrater,"intstar":z}
    return render(request,'details.html',{'x':x})  

def x_details_show(request,id):
    product=xprojectmodel.objects.get(id=id)
    reviews=reviewmodel.objects.filter(pid=id,department='xprojectmodel')
    print("<===============================>")
    a=[]
    t=0
    s5=0
    s4=0
    s3=0
    s2=0
    s1=0
    for n in range(len(reviews)):
        for i in  range(reviews[n].star):
            a.append(i)
        t=t+a[-1]+1
        if 5 == a[-1]+1:
            s5=s5+1
        elif 4 == a[-1]+1:
            s4=s4+1
        elif 3 == a[-1]+1:
            s3=s3+1
        elif 2 == a[-1]+1:
            s2=s2+1
        else:
            s1=s1+1
    if t != 0:
        avg=((t)/(len(reviews)*5))*100

        print(s5,s4,s3,s2,s1)
        avg5=(s5/len(reviews))*100
        avg4=(s4/len(reviews))*100
        avg3=(s3/len(reviews))*100
        avg2=(s2/len(reviews))*100
        avg1=(s1/len(reviews))*100
    else:
        avg=0
        avg5=0
        avg4=0
        avg3=0
        avg2=0
        avg1=0

    print(avg,avg5,avg4,avg3,avg2,avg1)
    totalrater=len(reviews)
    print("totalrater",avg)
    totalstar=((((avg)/2))/10)
    print("totalstar",totalstar)
    print("<===============================>")
    z=[]
    ss=round(totalstar)
    for i in range(ss):
        z.append(i)
    print(z)
    x={"product":product, "reviews":reviews,"avg":int(avg),"totalstar":round(totalstar,1),"avg5":avg5,"avg4":avg4,"avg3":avg3,"avg2":avg2,"avg1":avg1,"totalrater":totalrater,"intstar":z}
    return render(request,'details.html',{'x':x})  

def o_details_show(request,id):
    product=othermodel.objects.get(id=id)
    reviews=reviewmodel.objects.filter(pid=id,department='othermodel')
    print("<===============================>")
    a=[]
    t=0
    s5=0
    s4=0
    s3=0
    s2=0
    s1=0
    for n in range(len(reviews)):
        for i in  range(reviews[n].star):
            a.append(i)
        t=t+a[-1]+1
        if 5 == a[-1]+1:
            s5=s5+1
        elif 4 == a[-1]+1:
            s4=s4+1
        elif 3 == a[-1]+1:
            s3=s3+1
        elif 2 == a[-1]+1:
            s2=s2+1
        else:
            s1=s1+1
    if t != 0:
        avg=((t)/(len(reviews)*5))*100

        print(s5,s4,s3,s2,s1)
        avg5=(s5/len(reviews))*100
        avg4=(s4/len(reviews))*100
        avg3=(s3/len(reviews))*100
        avg2=(s2/len(reviews))*100
        avg1=(s1/len(reviews))*100
    else:
        avg=0
        avg5=0
        avg4=0
        avg3=0
        avg2=0
        avg1=0

    print(avg,avg5,avg4,avg3,avg2,avg1)
    totalrater=len(reviews)
    print("totalrater",avg)
    totalstar=((((avg)/2))/10)
    print("totalstar",round(totalstar))
    print("<===============================>")
    z=[]
    ss=round(totalstar)
    for i in range(ss):
        z.append(i)
    print(z)
    x={"product":product, "reviews":reviews,"avg":int(avg),"totalstar":round(totalstar,1),"avg5":avg5,"avg4":avg4,"avg3":avg3,"avg2":avg2,"avg1":avg1,"totalrater":totalrater,"intstar":z}
    return render(request,'details.html',{'x':x})  


def profile(request, user):
    user = User.objects.get(username=user)
    profile = profiles.objects.get(user_id=user.id)
    x={"u":user, "p":profile}
    return render(request, 'profile.html',{'x':x})

def update_profile(request, user):
    uname=request.POST.get('user_name')
    first=request.POST.get('first_name')
    last=request.POST.get('last_name')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    d = User.objects.get(username=user)
    user=User.objects.filter(username=user).update(username=uname, email=email, first_name=first, last_name=last)
    profile = profiles.objects.filter(user_id=d.id).update(phone=phone)
    print(user, uname, email, phone)
    print('successfully user Updated')
    messages.info(request,'successfully user Updated')
    return redirect('home')

def account_delete(request, user):
    userdelete=User.objects.get(username=user)
    profileuserdelete = profiles.objects.get(user_id=userdelete.id)
    profileuserdelete.delete()
    userdelete.delete()
    print('successfully account permanently deleted')
    messages.info(request,'successfully account permanently deleted')
    print("<===================>")
    return redirect('/')

def chatbox(request):
    return render(request,'chatbox.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

