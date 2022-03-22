from django.shortcuts import render
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
    
    
   
    obj=signup.objects.get(sid=id)
    return render(request,'index2.html',{'user':obj,})
