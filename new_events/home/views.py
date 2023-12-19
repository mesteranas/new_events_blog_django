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
    if r.method=="POST":
        frm=forms.new_accound(r.POST)
        if frm.is_valid():
            fristName=frm.cleaned_data["frist_name"]
            lastName=frm.cleaned_data['last_name']
            email=frm.cleaned_data["email"]
            userName=frm.cleaned_data["user_name"]
            bio=frm.cleaned_data["bio"]
            gender=frm.cleaned_data["gender"]
            password=frm.cleaned_data["password"]
            confpassword=frm.cleaned_data["confpassword"]
            if not User.objects.filter(username=userName).exists():
                if password==confpassword:
                    user=User.objects.create_user(userName,email,password,first_name=fristName,last_name=lastName)
                    profile=models.Profile(user=user,bio=bio,gender=gender)
                    profile.save()
                    auth.login(r,user)
                    return redirect("homePage")

    frm=forms.new_accound()
    return render(r,"new-user.html",{"form":frm})
def blog(r):
    posts=models.post.objects.all().order_by("-date")
    return render(r,"blog.html",{"posts":posts})
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
    if r.method=="POST":
        frm=forms.RAddPost(r.POST)
        if frm.is_valid():
            title=frm.cleaned_data["title"]
            body=frm.cleaned_data["content"]
            resources=frm.cleaned_data["resources"]
            category=frm.cleaned_data["category"]
            user1=get_object_or_404(User,username=r.user)
            if user1.is_superuser:
                view=True
            else:
                view=False
            pubPost=models.post(title=title,body=body,resources=resources,category=category,is_view=view,user=user1)
            pubPost.save()
            profi=get_object_or_404(models.Profile,user=user1)
            profi.postsCount+=1
            profi.save()
            return redirect("ViewPost",pk=pubPost.pk)
    frm=forms.RAddPost()
    return render(r,"readdpost.html",{"form":frm})
def viewblog(r,pk):
    if r.method=="POST":
        re=r.POST["re"]
        EPost=get_object_or_404(models.post,pk=pk)
        if re=="view":
            EPost.is_view=True
        elif re=="like":
            EPost.like+=1
        elif re=="deslike":
            EPost.deslike+=1
        EPost.save()
    post=get_object_or_404(models.post,pk=pk)
    return render(r,"post.html",{"post":post})
def hidenblog(r):
    posts=models.post.objects.all().order_by("-date")
    return render(r,"hiddenPost.html",{"posts":posts})
def getuser(r,user_name):
    user1=get_object_or_404(User,username=user_name)
    post=models.post.objects.filter(user=user1).order_by("-date")
    user_=get_object_or_404(models.Profile,user=user1)
    return render(r,"user.html",{"User":user_,"User1":user1,"posts":post})
@login_required
def settings(r):
    return render(r,"profile.html")
@login_required
def deletacc(r):
    if r.method=="POST":
        frm=forms.delete(r.POST)
        if frm.is_valid():
            password=frm.cleaned_data["password"]
            user1=User.objects.get(username=r.user)
            if user1.check_password(password):
                User.delete(user1)
                return redirect("homePage")
    frm=forms.delete()
    return render(r,"deleteAccount.html",{"form":frm})
@login_required
def changePassword(r):
    if r.method=="POST":
        frm=forms.ChangePassword(r.POST)
        if frm.is_valid():
            password=frm.cleaned_data["currentPassword"]
            newpassword=frm.cleaned_data["newPassword"]
            confnewpassword=frm.cleaned_data["confNewPassword"]
            user1=User.objects.get(username=r.user)
            if user1.check_password(password):
                if newpassword==confnewpassword:
                    user1.set_password(newpassword)
                    user1.save()
                    auth.login(r,user1)
                    return redirect("homePage")
    frm=forms.ChangePassword()
    return render(r,"change_password.html",{"form":frm})
@login_required
def changeProfiel(r):
    user1=User.objects.get(username=r.user)
    profile=models.Profile.objects.get(user=user1)
    if r.method=="POST":
        frm=forms.editProfile(r.POST)
        if frm.is_valid():
            firstname=frm.cleaned_data["first_name"]
            lastname=frm.cleaned_data["last_name"]
            email=frm.cleaned_data["email"]
            bio=frm.cleaned_data["bio"]
            user1.first_name=firstname
            user1.last_name=lastname
            user1.email=email
            user1.save()
            profile.bio=bio
            profile.save()
            return redirect("GetUser",user_name=r.user)
    frm=forms.editProfile({"first_name":user1.first_name,"last_name":user1.last_name,"email":user1.email,"bio":profile.bio})
    return render(r,"change_profile.html",{"form":frm})