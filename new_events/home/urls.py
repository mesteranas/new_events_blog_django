from django.urls import path
from . import views
urlpatterns=[
    path("",views.home_,name="homePage"),
    path("contect/",views.Contect,name="contect"),
    path("about/",views.about,name="about"),
    path("accounds/new",views.newaccound,name="newaccound"),
    path("accound/login",views.login,name="login"),
    path("blog",views.blog,name="blog"),
    path("post/requestAdd",views.readdpost,name="rAddPost"),
    path("accound/logout",views.logout,name="logout")
]