from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from form.models import Accountholders
from django.contrib.auth import authenticate,login,logout


def index(request):
    return render(request,'signup.html')

def signIn(request):
    if request.method == 'POST':
        lnamee = request.POST['lname']
        lpasss = request.POST['lpass']
        
        user=authenticate(username=lnamee, password=lpasss)
        if user is not None:
            login(request, user)
            messages.success(request, "login succesfully!!!")
            return render(request,'wizart.html')
        else:
            messages.error(request, "invalid user....") 
            return redirect('home')
    return HttpResponse("404- Not found")
    
def signUp(request):
    if request.method == 'POST':
        name=request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        
        user=User.objects.create_user(name,email,pass1)
        user.save()
        messages.success(request,"Signup succesful!")
        return render(request,'wizart.html')
    else:
       return HttpResponse("404 - Not found")
        
    
def handle_submit(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        number = request.POST['number']
        gender=request.POST['gender']
        fathername = request.POST['fathername']
        smdId = request.POST['smdId']
        pan = request.POST['pan']
        date=request.POST['date']
        adhar = request.POST['adhar']
        nName = request.POST['nName']
        age = request.POST['age']
        relation = request.POST['relation']
        accNo=request.POST['accNo']
        ifsc = request.POST['ifsc']
        hno = request.POST['hno']
        address = request.POST['address']
        browser = request.POST['browser']
        city = request.POST['city']
        landmark = request.POST['landmark']
        
        
        user=Accountholders(firstName =fname,lastname=lname, email=email,number=number,gender=gender,fathername=fathername,smdId=smdId,pan=pan,date=date,adhar=adhar,nName=nName,age=age,relation=relation,
                            accNo=accNo,ifsc=ifsc,hno=hno,address=address,browser=browser,city=city,landmark=landmark)
        user.save()
        messages.success(request,"Data submit succesful!")
        return render(request,'wizart.html')
    else:
       return HttpResponse("404 - Not found")
        


def user_logout(request):
        logout(request)
        messages.success(request, "Successfully logged out")
        return redirect('authhome')

def user_choice(request,choice):
    if choice == 'login':
       return signIn(request)
    elif choice == 'signup':
       return signUp(request)
    
    elif choice == 'logout':
       return user_logout(request)
    elif choice == 'submit':
       return  handle_submit(request)

# Create your views here.
