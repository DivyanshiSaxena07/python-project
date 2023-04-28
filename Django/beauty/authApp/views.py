from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.

def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        user=User.objects.create_user(name, email, pass1)
        user.save()
        messages.success(request,"signup succesfully!!!")
        return redirect('authhome')

    else:
       return HttpResponse("404 - Not found")

        
        
def user_login(request):
 if request.method == 'POST':
    lname=request.POST['lname']
    lpass=request.POST['lpass']
    
    user=authenticate(username=lname, password=lpass)
    if user is not None:
        login(request, user)
        messages.success(request, "login succesfully!!!")
        return redirect('authhome')
    else:
        messages.error(request, "invalid user....")
        return redirect('authhome')
 return HttpResponse("404- Not found")
     
            
def user_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('authhome')     
        
    
    

def userchoice(request, choice):
    if choice == 'signup':
        return signup(request)
    
    elif choice == 'login':
        return user_login(request)
    
    elif choice == 'logout':
        return user_logout(request)
    
    else:
        return HttpResponse("<h2> not found request....</h2>")

















# def handleSignUp(request):
#     return render(request,'indx.html')
#     # if request.method == 'POST':
#     #     name = request.POST['name']
#     #     email = request.POST['email']
#     #     pass1 = request.POST['pass1']
#     #     pass2 = request.POST['pass2']
        
#     # if len(name)<3:
#     #   pass        
#     # if pass1!=pass2:
#     #     pass
    
#     # myUser=User.objects.create_user(name,email, pass1)
#     # myUser.
    
            