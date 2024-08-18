from django.urls import path
from . import views

urlpatterns = [
    path('login_admin/', views.login_admin, name="login_admin"),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('logout_admin/', views.log_out, name="logout_admin"),
]
