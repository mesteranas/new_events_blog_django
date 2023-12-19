from django.urls import path
from . import views
urlpatterns=[
    path("",views.home_,name="homePage"),
    path("contect/",views.Contect,name="contect"),
    path("about/",views.about,name="about"),
    path("accounts/new",views.newaccound,name="newaccound"),
    path("accounts/login",views.login,name="login"),
    path("blog",views.blog,name="blog"),
    path("post/requestAdd",views.readdpost,name="rAddPost"),
    path("accounts/logout",views.logout,name="logout"),
    path("post/<int:pk>",views.viewblog,name="ViewPost"),
    path("blog/hiden",views.hidenblog,name="hiddenPost"),
    path("user/<str:user_name>",views.getuser,name="GetUser"),
 path("accounts/settings",views.settings,name="accountSettings")   ,
 path("accounts/delete",views.deletacc,name="deleteaccount"),
 path("accounts/changePassword",views.changePassword,name="changePassword"),
 path("accounts/editProfile",views.changeProfiel,name="changeProfile")
]