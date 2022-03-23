
from django.shortcuts import render,redirect
from .models import signup
# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST['nme']
        adr=request.POST['adr']
        phno=request.POST['phn']
        emil=request.POST['eml']
        usn=request.POST['usrn']
        psw=request.POST['pwd']
        obj=signup(name=name,address=adr,phno=phno,email=emil,uname=usn,pwd=psw)
        obj.save()

    return render(request,'index.html')

def index1(request):

    data=signup.objects.all()
    if request.method=='POST':
        id=request.POST['id']
        obj=signup.objects.filter(sid=id)
        obj.delete()
    return render(request,'index1.html',{'user':data,})

def fb(request):
    return render(request,'facebook.html')

def index2(request,id):
    if request.method=='POST':
        name=request.POST['nme']
        id=request.POST['id']
        adr=request.POST['adr']
        phno=request.POST['phn']
        emil=request.POST['eml']
        usn=request.POST['usrn']
        psw=request.POST['pwd']
        # obj=signup(name=name,address=adr,phno=phno,email=emil,uname=usn,pwd=psw)
        # obj.save()
        obj=signup.objects.get(sid=id)
        obj.name=name
        obj.adrs=adr
        obj.pno=phno
        obj.email=emil
        obj.usrid=usn
        obj.pwd=psw
        obj.save()

    
   
    obj=signup.objects.get(sid=id)
    return render(request,'index2.html',{'user':obj,})



def login(request):
    msg=""
    if request.method=='POST':
        # print('hhhh')
        usrname=request.POST['username']
        passwrd=request.POST['pwd']
        # obj_exist=signup.objects.filter(uname=usrname,pwd=passwrd).exists()
        # if obj_exist:
        #     return redirect("home")
        # else:
        #     msg="Username or password incorrect"
        try:
            obj_exist=signup.objects.get(uname=usrname,pwd=passwrd)
            request.session['user']=obj_exist.sid
            return redirect("home")
        
        except signup.DoesNotExist:
            msg="Username or password incorrect"

    return render(request,"login.html",{'msg':msg,})

def home(request):
    obj=signup.objects.get(sid=request.session['user'])
    return render(request,"home.html",{'user':obj,})


def logout(request):
    del  request.session['user']
    request.session.flush()
    
    return redirect("log_user")

def prof(request):
    obj=signup.objects.get(sid=request.session['user'])
    print(obj)
    if request.method=='POST':
        # id=request.session['id']
        name=request.POST['nme']
        adr=request.POST['adr']
        phno=request.POST['phn']
        emil=request.POST['eml']
        usn=request.POST['usrn']
        psw=request.POST['pwd']
        # obj=signup(name=name,address=adr,phno=phno,email=emil,uname=usn,pwd=psw)
        # obj.save()
        obj.name=name
        obj.adrs=adr
        obj.pno=phno
        obj.email=emil
        obj.usrid=usn
        obj.pwd=psw
        obj.save()
        return redirect("home")
        
    return render(request,"profile.html",{'user':obj})


def chpwd(request):
    msg=""
    if request.method=='POST':
     oldpwd=request.POST['chpsd']
     newpwd=request.POST['npsd']
     conpwd=request.POST['cpsd']
     obj=signup.objects.get(sid=request.session['user'])
     curpwd=obj.pwd
     if curpwd==oldpwd:
         if newpwd==conpwd:
             signup.objects.filter(sid=request.session['user']).update(pwd=newpwd)
             msg="password changed"
         else:
             msg="password does not match"
     else:
         msg="old password does not match"





    return render(request,"changepwd.html",{'msg':msg} )