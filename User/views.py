from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .form import UserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
# Create your views here.
def index(request):
    if request.method=="POST":
        fm=UserForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created successfully')
            fm.save()
    else:
        fm=UserForm()
    return render(request,'index.html',{'form':fm})
#login 
def User_login(request):
    if not request.user.is_authenticated: 
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass) 
                if user is not None:
                    login(request,user)
                    messages.success(request,'LoggedIn successfully')
                    return HttpResponseRedirect('/post/')
        fm=AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/post/')       

def post(request):
    if request.user.is_authenticated:
            userList=User.objects.values()
            if request.method=="POST":
                userList =User.objects.values()
            return render(request,'post.html',{'userList':userList})    
    else:
        userList=User.objects.all()
    return render(request,'post.html',{'userList':userList})
def user_logout(request):
    logout(request)
    messages.success(request,'Logged Out successfully')
    return HttpResponseRedirect('/login/')

#change pass
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password changed success fully ')

                return HttpResponseRedirect('/post/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def editPost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=UserForm(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
        else:
            fm=UserForm(instance=request.user)
        return render(request,'edit.html',{'form':fm,'name':request.user})

def del_user(request):    
        if request.user.is_authenticated:
            if request.method=="POST":
             fm=User.objects.get(request.POST,instance=request.User)
             if fm.is_valid():
                fm.delete()
            messages.success(request, "The user is deleted") 
        return HttpResponseRedirect('/login/')

