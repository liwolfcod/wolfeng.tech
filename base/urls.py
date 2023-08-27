from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout', views.Logout, name="logout"),
    path('about/', views.About, name="about"),
    path('blog/', views.Blog, name="blog"),
    path('contact/', views.Contact, name="contact"),
    path('adminpanel/', views.AdminPanel, name="adminpanel"),
    path('dashboard/', views.Dashboard, name="dashboard"),
    path('messages/', views.Messages, name="messages"),
    path('delete_message/<str:pk>/',views.delete_message, name="delete_message"),
    path('add_blog/', views.AddBlog, name="add_blog"),
    path('update_blog/<str:pk>/',views.update_blog, name="update_blog"),
    path('delete_blog/<str:pk>/',views.delete_blog, name="delete_blog"),
    path('blog/<str:pk>/', views.BlogPage, name= "blogpage"),
]
