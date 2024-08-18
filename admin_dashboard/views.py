from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_admin(request):
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')

    return render(request, template_name='admin/login_admin.html')


@login_required
def admin_dashboard(request):

    return render(request, template_name='admin/adminpanel.html')

def log_out(request):
    logout(request)
    return redirect('home') 