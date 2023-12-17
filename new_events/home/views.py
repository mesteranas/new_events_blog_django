from django.shortcuts import render,redirect,get_object_or_404
from . import forms,models
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def home_(r):
    return render(r,"home.html")
def Contect(r):
    return render(r,"contect.html")
def about(r):
    return render(r,"about.html")
def newaccound(r):
    frm=forms.new_accound()
    return render(r,"new-user.html",{"form":frm})
def blog(r):
    return render(r,"blog.html")
def login(r):
    if r.method=="POST":
        frm=forms.login(r.POST)
        if frm.is_valid():
            user_name=frm.cleaned_data["user_name"]
            password=frm.cleaned_data["password"]
            user=auth.authenticate(username=user_name,password=password)
            if user:
                auth.login(r,user)
                return redirect("homePage")
    frm=forms.login()
    return render(r,"login.html",{"form":frm})
@login_required
def logout(r):
    auth.logout(r)
    return redirect("homePage")
@login_required
def readdpost(r):
    return render(r,"readdpost.html")