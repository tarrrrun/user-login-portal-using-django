from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from myPortal.alchemy_configg import session
from .models import myModel


# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    mydb=myModel()
    
    if request.method=='POST':
        username=request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email=request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        phoneNum=request.POST['phonenum']
        company=request.POST['company']
        print(username)
        print(pass1)
        print(email)
        new_item=myModel(fname=fname)
        session.add(new_item)
        session.commit()
        if pass1==pass2:
            myUser = User.objects.create_user(username,pass1)

            myUser.email=email

            myUser.first_name=fname
            myUser.last_name=lname

            myUser.save()
            messages.success(request,"Your account has been successfully created.")
            return redirect('signin')
        else:
            messages.success(request,"password does not match")
            redirect("signup")

    return render(request,"authentication/signup.html")

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user = authenticate(request,username=username,password=pass1)
        print(user)
        print(pass1)
        print(username)
        if user is not None:
            login(request,user)
            fname=user.first_name
            company=user.company
            return render(request,"authentication/index.html",{'fname':fname,'company':company})
        else:
            messages.error(request,"Wrong credentials")
            return redirect("home")

    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')