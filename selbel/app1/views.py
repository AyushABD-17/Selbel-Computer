from django.shortcuts import render,redirect
from django.contrib import messages
from app1.models import services,team,Contact

# Create your views here.

def home(request):
    teams = team.objects.all()
    context = {'teams':teams}
    return render(request,'index.html',context)

def service(request):
    service = services.objects.all()
    context = {'service':service}
    return render(request,'service.html',context)

def teams(request):
    teams = team.objects.all()
    context = {'teams':teams}
    return render(request,'team.html',context)

def contact(request):
    if request.method =="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fsubject=request.POST.get('subject')
        fmsg=request.POST.get('message')
        query = Contact(name = fname,email= femail,phonenumber = fphoneno,subject=fsubject,msg=fmsg)
        query.save()
        messages.info(request,"we will get you soon")
        return redirect("/contact")
        


    return render(request,'contact.html')

# About Page:
def about(request):
    token = team.objects.all()
    context = {'token':token}
    return render(request,'about.html',context)