from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('resume/', views.resume, name="resume"),
    path('profile/', views.profile_dashboard, name="profile_dashboard"),
    path('userlist/', views.user_list, name="userlist"),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('signout/', views.sign_out, name="signout"),
    path('test/', views.test),
]
