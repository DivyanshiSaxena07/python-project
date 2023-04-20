from django.shortcuts import render,HttpResponse,redirect
from product.models import Contact
from django.db import models
from datetime import datetime
from django.contrib import messages
from product.models import Customer


def index(request):
   return render(request,'index.html')

def about(request):
 return render(request,'about.html')

def contact(request):
   if request.method == 'POST':
      
      name=request.POST.get('name')
      email=request.POST.get('email')
      subject=request.POST.get('subject')
      phone=request.POST.get('phone')
      msg=request.POST.get('message')
      contact=Contact(name=name,email=email,phone=phone,msg=msg, subject=subject, date=datetime.today())
      contact.save()
   
      messages.success(request,"form Submittd")
   return render(request,'contact.html')


def view(request):
   custm=Customer.objects.all()
   return render(request,'insertItem.html',{'customers': custm})

def add(request):
   if request.method == 'POST':
      name=request.POST.get('name')
      email=request.POST.get('email')
      address=request.POST.get('address')
      phone=request.POST.get('phone')
      
      customer=Customer(name=name,email=email,address=address,phone=phone)
      customer.save()
      custm=Customer.objects.all()
   return render(request,'insertItem.html',{'customers': custm})   

def edit(request):
   custm=Customer.objects.all()
   return render('insertItem.html',{'customers':custm})
   
def update(request,id):
      if request.method == 'POST':
         name=request.POST.get('name')
         email=request.POST.get('email')
         address=request.POST.get('address')
         phone=request.POST.get('phone')
         
         customer=Customer(id=id,name=name,email=email,address=address,phone=phone)
         custm=Customer.objects.all()
         customer.save()
      return render(request,'insertItem.html',{'customers': custm})   
   

def delete(request,id):
   cust=Customer.objects.filter(id=id)
   cust.delete()
   
   return redirect('view')