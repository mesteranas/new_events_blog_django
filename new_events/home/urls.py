from django.urls import path
from . import views
urlpatterns=[
    path("",views.home_,name="homePage"),
    path("contect/",views.Contect,name="contect"),
    path("about/",views.about,name="about"),
    path("accounds/new",views.newaccound,name="newaccound"),
    path("accounds/login",views.login,name="login"),
    path("blog",views.blog,name="blog"),
    path("post/requestAdd",views.readdpost,name="rAddPost"),
    path("accounds/logout",views.logout,name="logout"),
    path("post/<int:pk>",views.viewblog,name="ViewPost"),
    path("blog/hiden",views.hidenblog,name="hiddenPost"),
    path("user/<str:user_name>",views.getuser,name="GetUser"),
 path("account/settings",views.settings,name="accountSettings")   ,
 path("account/delete",views.deletacc,name="deleteaccount"),
]